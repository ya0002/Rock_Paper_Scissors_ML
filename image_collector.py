import cv2
import keyboard
import os

def save_image(type_file, sample, n_samples_collected, frame,n_images):
    if n_images>(0.7*500):
        os.chdir(current_dir + '\\' +'Dataset'+'\\'+dataset_type[1]+'\\'+ file_name[type_file])
    else:
        os.chdir(current_dir + '\\' +'Dataset'+'\\'+dataset_type[0]+'\\'+ file_name[type_file])
    cv2.imwrite(f'{file_name[type_file]}{n_samples_collected}.png', frame[105:395, 285:595])
    n_samples_collected += 1
    n_images +=1
    if n_images == 500:
        sample = False
        n_images=0
    return sample, n_samples_collected,n_images


# creating files to store the images in

current_dir=os.getcwd()

dataset_type=['train','validation']
file_name=['rock','paper','scissor','dummy']
try:
    os.mkdir(current_dir + '\\' + 'Dataset')
    for name in dataset_type:
        os.mkdir(current_dir+'\\'+'Dataset'+'\\'+name)
        for i in file_name:
            os.mkdir(current_dir + '\\' +'Dataset'+'\\'+name+'\\'+ i)
except:
    pass


Rock,Paper,Scissor,Dummy=False,False,False,False
n_Rock,n_Paper,n_Scissor,n_Dummy,n_images=0,0,0,0,0

vid=cv2.VideoCapture(0)
while True:
    success, frame=vid.read()
    if not success:
        print('ERROR')
        break

    frame=cv2.flip(frame,1)
    cv2.putText(frame, 'Rock: '+str(n_Rock), (10, 26), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, 'Paper: '+str(n_Paper), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, 'Scissors: '+str(n_Scissor), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, 'Dummy: '+str(n_Dummy), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.rectangle(frame,(280,100),(600,400),(0,0,255),2)
    cv2.imshow('video', frame)

    if keyboard.is_pressed('r'):
        if (Paper,Scissor,Dummy)==(False,False,False):
            Rock=True
            print('collecting rock')
        else:
            print('unavailable right now')

    if Rock:
        Rock,n_Rock,n_images=save_image(0,Rock,n_Rock,frame,n_images)


    if keyboard.is_pressed('p'):
        if (Rock,Scissor,Dummy)==(False,False,False):
            Paper=True
            print('collecting paper')
        else:
            print('unavailable right now')

    if Paper:
        Paper,n_Paper,n_images=save_image(1,Paper,n_Paper,frame,n_images)


    if keyboard.is_pressed('s'):
        if (Rock,Paper,Dummy)==(False,False,False):
            Scissor=True
            print('collecting scissor')
        else:
            print('unavailable right now')

    if Scissor:
        Scissor,n_Scissor,n_images=save_image(2,Scissor,n_Scissor,frame,n_images)


    if keyboard.is_pressed('d'):
        if (Rock,Paper, Scissor) == (False,False, False):
            Dummy = True
            print('collecting dummy')
        else:
            print('unavailable right now')

    if Dummy:
        Dummy, n_Dummy, n_images = save_image(3, Dummy, n_Dummy, frame, n_images)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
