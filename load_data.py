# coding=utf-8
'''
Module Name:load_data
Function:to load the data from dataset obtained during quarter-final
Remark:we must use encoding utf-8 in that the filename of lyrics is in Chinese.
       However, we don't want to use Chinese in any corner of our program.
'''

import pandas as pd
import numpy as np
import os

'''
Function name:Training_Set
Task:to load the training data from dataset
Input:None
Output: A pandas.DataFrame including training data and their labels
'''


def Training_Set():
    path = 'data\\TrainingData'
    Emotion = ['Athrill', 'Calm', 'Gloomy', 'Lyric', 'Pleasant']
    Pd_dataframe = pd.DataFrame(
        columns=[
            'word%d' %
            (x +
             1) for x in range(1500)].append(
            ['Label']))
    for Each_emotion in Emotion:  # load data from various sets of emotion
        Each_path = path + '\\' + Each_emotion
        Data_dir = os.listdir(Each_path)
        # A matrix with the size of (number of lyric)*1500
        Each_npmatrix = [[0 for _ in range(1500)]
                         for _ in range(len(Data_dir))]
        for Each_lyric in range(len(Data_dir)):
            f = open(Each_path + "\\%s" % (Data_dir[Each_lyric]))
            Single_data = f.readlines()
            Each_npmatrix[Each_lyric] = [
                int(x[:-1]) for x in Single_data]  # Eliminate "\n"
            f.close()
        Np_matrix = np.array(Each_npmatrix)
        Each_dataframe = pd.DataFrame(
            Np_matrix, columns=[
                'word%d' %
                (x + 1) for x in range(1500)])
        Each_dataframe['Label'] = Each_emotion  # the emotion label of data
        Pd_dataframe = pd.concat(
            [Pd_dataframe, Each_dataframe], ignore_index=True)
    return Pd_dataframe


'''
Function name:Testing_Set
Task:to load the testing data from dataset
Input:None
Output: A pandas.DataFrame including testing lyric(string) and their labels
'''


def Testing_Set():  # the code is similar to function"Training_Set"
    path = 'data\\TestingData'
    Emotion = ['Athrill', 'Calm', 'Gloomy', 'Lyric', 'Pleasant']
    Pd_dataframe = pd.DataFrame(columns=['Lyric', 'Label'])
    for Each_emotion in Emotion:
        Each_path = path + '\\' + Each_emotion
        Data_dir = os.listdir(Each_path)
        Each_npmatrix = [[''] for _ in range(len(Data_dir))]
        for Each_lyric in range(len(Data_dir)):
            f = open(Each_path + "\\%s" % (Data_dir[Each_lyric]))
            Single_data = f.readlines()
            Each_npmatrix[Each_lyric] = [int(x[:-1]) for x in Single_data]
        Np_matrix = np.array(Each_npmatrix)
        Each_dataframe = pd.DataFrame(Np_matrix, columns=['Lyric'])
        Each_dataframe['Label'] = Each_emotion
        Pd_dataframe = pd.concat(
            [Pd_dataframe, Each_dataframe], ignore_index=True)
    return Pd_dataframe
