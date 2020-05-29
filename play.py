import cv2
import keyboard
import os
import tensorflow as tf
import cv2
import numpy as np

model=tf.keras.models.load_model('rock_paper_scissor.h5')

move={0:'nothing',1:'paper',2:'rock',3:'scissor'}

vid=cv2.VideoCapture(0)
while True:
    success, frame=vid.read()
    if not success:
        print('ERROR')
        break

    frame=cv2.flip(frame,1)
    # cv2.putText(frame, 'Rock: '+str(n_Rock), (10, 26), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.rectangle(frame,(280,100),(600,400),(0,0,255),2)
    cv2.imshow('video', frame)

    img_predict=frame[105:395, 285:595]
    img_predict = np.reshape(img_predict, (1, 290, 310, 3))
    prediction=model.predict(img_predict)
    print(prediction)
    index = np.argmax(prediction)
    print(index, move[index])

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

