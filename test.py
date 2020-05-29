import tensorflow as tf
import cv2
import numpy as np

model=tf.keras.models.load_model('rock_paper_scissor.h5')

move={0:'nothing',1:'paper',2:'rock',3:'scissor'}

#reading the image
img=cv2.imread(r'path to an image')

# reshaping it
img=cv2.resize(img,(290,310))
img_predict=np.reshape(img,(1,290,310,3))
print(img.shape)
print(img_predict.shape)

print(model.predict(img_predict))
index=np.argmax(model.predict(img_predict))
print(index,move[index])

cv2.imshow('image',img)
cv2.waitKey(0)