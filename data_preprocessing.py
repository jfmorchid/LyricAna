# coding=utf-8
'''
Module Name:data_preprocessing
Function: preprocess the training data(input && ideal one-hot output)
'''

import pandas as pd
from load_data import Training_Set

'''
Function name:One_Hot
Task:to convert label into an ont-hot format
Input:The pandas.DataFrame of training data
Output:Two pandas.DataFrames including training data and their ONE-HOT labels
'''


def One_Hot(Training_data):
    # Column:one-hot code of the label (5 categories)
    Onehot_label = [[0 for _ in range(5)] for _ in range(len(Training_data))]
    for x in range(len(Training_data)):
        # Order:Athrill,Calm,Gloomy,Lyric,Pleasant
        Label = Training_data['Label'][x]
        if(Label == 'Athrill'):
            Onehot_label[x] = [1, 0, 0, 0, 0]
        elif(Label == 'Calm'):
            Onehot_label[x] = [0, 1, 0, 0, 0]
        elif(Label == 'Gloomy'):
            Onehot_label[x] = [0, 0, 1, 0, 0]
        elif(Label == 'Lyric'):
            Onehot_label[x] = [0, 0, 0, 1, 0]
        elif(Label == 'Pleasant'):
            Onehot_label[x] = [0, 0, 0, 0, 1]
    Training_label = pd.DataFrame(
        Onehot_label,
        columns=[
            'Athrill',
            'Calm',
            'Gloomy',
            'Lyric',
            'Pleasant'])
    return Training_data.drop('Label', axis=1), Training_label
