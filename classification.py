# -*- coding: utf-8 -*-
"""Classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z0d-2_WiP547kN4HGBKHZMtO1XfUz0vx

# Install TF 2.0
"""

!pip install -q tensorflow==2.0.0-beta1

"""# import packages"""

import tensorflow as tf
print(tf.__version__)

from sklearn.datasets import load_breast_cancer

"""#Import Data"""

data=load_breast_cancer()
data.keys()

data.data.shape

data.target

data.target_names

data.target.shape

data.feature_names

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(data.data,data.target,test_size=0.33)

N,D=x_train.shape
N
D

from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()
scaler
x_train = scaler.fit_transform(x_train)
x_train
x_test= scaler.fit_transform(x_test)

model=tf.keras.models.Sequential([tf.keras.layers.Input(shape=(D,)),tf.keras.layers.Dense(1,activation="sigmoid")])
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
r=model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=100)

print(model.evaluate(x_test,y_test))
print(model.evaluate(x_train,y_train))

import matplotlib.pyplot as plt
plt.plot(r.history['loss'],label='loss')
plt.plot(r.history['val_loss'],label='val_loss')
plt.legend()

plt.plot(r.history['accuracy'],label='accuracy')
plt.plot(r.history['val_accuracy'],label='val_accuracy')
plt.legend()