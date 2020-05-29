
import os
import cv2
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.applications.vgg16 import VGG16 as pre_trained_model, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#setting the paths
current=os.getcwd()
train_path = current+'\\'+'Dataset'+'\\'+'train'
validation_path = current+'\\'+'Dataset'+'\\'+'validation'

#getting the image shape
img=cv2.imread(train_path+'\\'+'rock'+'\\'+'rock2.png')
img_size=list(img.shape)[:-1]


#for getting the number of classes
classes=len(os.listdir(train_path))

ptm=pre_trained_model(input_shape=img_size+[3]
                      ,weights='imagenet'
                      ,include_top=False)
ptm.trainable=False

x=Flatten()(ptm.output)
x=Dense(classes,activation='softmax')(x)

model=Model(inputs=ptm.input,outputs=x)

model.summary()

# instance image generator
gen=ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    preprocessing_function=preprocess_input
    )

Batch_size=128

train_generator=gen.flow_from_directory(
    train_path,
    shuffle=True,
    target_size=img_size,
    batch_size=Batch_size)

valid_generator=gen.flow_from_directory(
    validation_path,
    target_size=img_size,
    batch_size=Batch_size)

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
    )

# adding early stopping
from tensorflow.keras.callbacks import EarlyStopping

early_stop=EarlyStopping(monitor='val_loss',patience=2)


#fit model
results=model.fit_generator(
    train_generator,
    validation_data=valid_generator,
    epochs=25,
    callbacks=[early_stop]
    )

#accuracy= approx 90%

# model.save('rock_paper_scissor.h5')
