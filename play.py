import keyboard
import tensorflow as tf
import cv2
import numpy as np
import random
import os

current=os.getcwd()

model=tf.keras.models.load_model('rock_paper_scissor.h5')

move={0:'nothing',1:'paper',2:'rock',3:'scissor'}
move_cartoon=[cv2.imread(current+'\\'+'Props'+'\\'+'dummy.PNG'),cv2.imread(current+'\\'+'Props'+'\\'+'paper.PNG'),cv2.imread(current+'\\'+'Props'+'\\'+'rock.PNG'),cv2.imread(current+'\\'+'Props'+'\\'+'scissor.PNG')]

#initialize it to dummy.PNG
img_cartoon=move_cartoon[0]

n_frame,index,c_index=[0]*3
points=[0,0]  # index=0 for computer   and index=1 for user(YOU)
vid=cv2.VideoCapture(0)
while True:
    success, frame=vid.read()
    if not success:
        print('ERROR')
        break

    frame=cv2.flip(frame,1)

    frame[0:480,0:278]=img_cartoon
    frame[404:480,278:640]=np.full((76,362,3),255)
    frame[0:404,603:640]=np.full((404,37,3),255)
    frame[0:101,278:603]=np.full((101,325,3),255)

    # if you wanna keep the transparency  P.S=Black won't show     I didn't do it because my hardware wasn't upto it, it was lagging a lot
    # for i in range(200):
    #     for j in range(200):
    #         x=img_cartoon[i,j]
    #         if list(x)!=[0,0,0]:
    #             frame[i, j] = x

    cv2.putText(frame, 'Your Move: ' + move[index], (450, 26), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0), 1)
    cv2.putText(frame, 'Computer: ' + move[c_index], (10, 26), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 0), 1)
    cv2.putText(frame, f'{points[0]} - {points[1]}', (280, 26), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.rectangle(frame,(280,100),(600,400),(0,0,255),2)
    cv2.imshow('video', frame)

    if keyboard.is_pressed('r'):
        points=[0,0]

    if n_frame % 50 == 0:
        img_predict=frame[105:395, 285:595]
        img_predict = np.reshape(img_predict, (1, 290, 310, 3))
        prediction=model.predict(img_predict)
        print(prediction)
        index = np.argmax(prediction)
        print(index, move[index])
        if index!=0:
            c_index=random.randint(1,3)
            img_cartoon = move_cartoon[c_index]
            if index!=c_index:
                if (index,c_index)!=(1,3) and (index,c_index)!=(3,1):
                    if index<c_index:
                        points[1]+=1
                    else:
                        points[0]+=1
                else:
                    if index==3:
                        points[1]+=1
                    else:
                        points[0]+=1
        else:
            c_index=0
            img_cartoon=move_cartoon[0]

    n_frame+=1

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

