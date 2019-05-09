# coding=utf-8
'''
Module Name:network_resnet
Function:Train a neuron network with ResNet

'''

import keras
from keras.layers import Dense, Add, BatchNormalization, Activation, Input
from keras.models import Model
from keras.constraints import min_max_norm

'''
Function name:Id_Block
Task:to build an identity mapping block with Dense
Input:a keras functional API
output: another keras functional API
Remark: "Identity mapping" means "En" in algebra,but here it means input data's size is equal to that in output data
'''


def Id_Block(X):
    X_copy = X    # make a copy of X

    X = Dense(
        1500, use_bias=True, kernel_constraint=min_max_norm(
            0, 0), bias_constraint=min_max_norm(
            0, 0.6))(X)
    X = Activation('relu')(X)

    X = Dense(
        1500, use_bias=True, kernel_constraint=min_max_norm(
            0, 0.6), bias_constraint=min_max_norm(
            0, 0.6))(X)
    X = Add()([X, X_copy])  # skip these layers
    X = Activation('relu')(X)

    return X


'''
Function name:Heap_Block
Task:to heap these Id blocks, and the comple a ResNet model
Input:number of samples
Output:a keras ResNet model
'''


def Heap_Block(Samples):
    Model_input = Input((1500,))

    X = Dense(
        1500, kernel_constraint=min_max_norm(
            0, 0.6), bias_constraint=min_max_norm(
            0, 0.6))(Model_input)  # Initial layer
    X = Activation('relu')(X)

    X = Id_Block(X)  # Starting the task of heaping blocks (3 times)
    X = Id_Block(X)
    X = Id_Block(X)
    X = Dense(5, activation='softmax')(X)  # Classification layer
    model = Model(inputs=Model_input, outputs=X)
    return model
