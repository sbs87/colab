# -*- coding: utf-8 -*-
"""ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WhbDWLwhsguKuDZyi6bCwN_cBFD4yl_x
"""

!pip install -q tensorflow-gpu==2.0.0-beta1

import tensorflow as tf
print(tf.__version__)

mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
print(x_train.shape)
#print(x_train[0:3,0:3,0:3])
#print(y_train[0:3])
import matplotlib.pyplot as plt
#print(x_train[1][:][:])
#plt.scatter(x_train[1][:][:],x_train[1][:][:])

x_test,x_train = x_test/255.0,x_train/255.0

model=tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),
                           tf.keras.layers.Dense(128,activation="relu"),
                           tf.keras.layers.Dropout(0,2),
                           tf.keras.layers.Dense(10,activation="softmax")])

model.compile(optimizer='adam',metrics=['accuracy'],loss='sparse_categorical_crossentropy')

r=model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=10)

plt.plot(r.history['loss'],label='loss')
plt.plot(r.history['val_loss'],label='val_loss')
plt.legend()

plt.plot(r.history['accuracy'],label='accuracy')
plt.plot(r.history['val_accuracy'],label='vall_accuracy')
plt.legend()

print(model.evaluate(x_test,y_test))

"""Come back for confuson matrix"""