# coding=utf-8
'''
Main Program
Function:to analyze the lyric--give an emotional label to any lyric in Chinese
'''

import numpy as np
from load_data import Training_Set, Testing_Set
from data_preprocessing import One_Hot
import network_resnet
import lyric_to_vector
from keras.models import load_model


def Training():  # The procedure of training neuron network
    Training_data = Training_Set()  # load training dataset
    # Dividing data into input and label
    Input_data, Input_label = One_Hot(Training_data)
    model = network_resnet.Heap_Block(len(Input_data))  # Getting model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy'])  # compiling model
    model.fit(
        Input_data.values,
        Input_label.values,
        batch_size=32,
        epochs=7)  # Training model
    model.save('model.hdf5')  # Saving model


def Predicting(Path):  # The procedure of predicting the result with model
    Vector = lyric_to_vector.Main_Process(Path)
    Model_input = np.array(Vector).reshape(1, 1500)
    model = load_model('model.hdf5')
    return model.predict(Model_input)

print(Predicting('lyric.txt'))