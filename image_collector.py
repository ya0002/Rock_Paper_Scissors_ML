import cv2
import keyboard
import os

# creating files to store the images in
file_name=['rock','paper','scissor']
current_dir=os.getcwd()
try:
    for i in file_name:
        os.mkdir(current_dir+'\\'+i)
except:
    pass

vid=cv2.VideoCapture(0)

n_frame=1
while True:
    success, frame=vid.read()
    if not success:
        print('ERROR')
        break

    frame=cv2.flip(frame,1)
    cv2.putText(frame,str(n_frame),(10,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
    cv2.rectangle(frame,(280,100),(600,400),(0,0,255),2)
    cv2.imshow('video', frame)

    print(n_frame,frame.shape)
    n_frame += 1

    if keyboard.is_pressed('r'):
        print('pressed')
        os.chdir(current_dir+'\\'+file_name[0])
        to_save=frame[100:400,280:600]
        cv2.imwrite('rock_test11.png',to_save)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
