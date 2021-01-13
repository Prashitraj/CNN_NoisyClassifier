# -*- coding: utf-8 -*-
"""CNN_Noisy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZGkcspTtRHLFcWO4ta0yOUw67JdFLKJ1
"""

import os
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn import metrics
import tensorflow as tf

datagen = ImageDataGenerator()
# prepare an iterators for each dataset
train_it = datagen.flow_from_directory('../data/simple/train/',target_size=(627, 392), class_mode='binary',batch_size=40)
# val_it = datagen.flow_from_directory('../data/simple/validation/',target_size=(627, 392), class_mode='binary',batch_size=40)
test_it = datagen.flow_from_directory('../data/simple/test/',target_size=(627, 392), class_mode='binary',batch_size=40)
ptest_it = datagen.flow_from_directory('../data/simple/p_test/',target_size=(627, 392), class_mode='binary',batch_size=40)

num_rows = 692
num_columns = 327
num_channels = 3
num_labels = 2
# Construct model 
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=2, input_shape=(num_rows, num_columns, num_channels), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))

model.add(Conv2D(filters=32, kernel_size=2, activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))

model.add(Conv2D(filters=64, kernel_size=2, activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))

model.add(Conv2D(filters=128, kernel_size=2, activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))
model.add(GlobalAveragePooling2D())

model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy', # Loss
              metrics=['binary_accuracy'])

# Display model architecture summary 
model.summary()

from keras.callbacks import ModelCheckpoint 
from datetime import datetime 

num_epochs = 20
num_batch_size = 40

checkpointer = ModelCheckpoint(filepath='../data/simple/models.keras', 
                               verbose=1, save_best_only=True)
start = datetime.now()

model.fit(train_it,steps_per_epoch=400,epochs = 10, validation_data=ptest_it,validation_steps= 40,callbacks=[checkpointer], verbose=1)


duration = datetime.now() - start
print("Training completed in time: ", duration)

loss = model.evaluate(test_it)

model.save('../data/simple/model1.keras')