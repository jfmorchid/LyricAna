# coding=utf-8
'''
Module Name:lyric_to_vector
Function: convert the lyric(in Chinese) into a vector
'''
import jieba.posseg


'''
Function name:Lyric_Load
Task:to load the lyric in "Lyric.txt"
Input:the path of lyric text
Output:an entire string including the lyric
'''


def Lyric_Load(Path):
    f = open(Path)
    Lyric, Data = f.readlines(), ''
    for Sentence in Lyric:
        Data = Data + Sentence
    return Data


'''
Function name:Cut_Word
Task:to cut the lyric into seperate words
Input: the lyric
Output: a list of useful words
'''


def Cut_Word(text):
    Sentence = jieba.posseg.cut(text)
    f = open("data\\stop_word.txt")  # import the library of stop words
    Tingyong = f.read()
    # we merely use the words with these parts of speech
    ValidFlag = ['a', 'ad', 'an', 'd', 'g', 'i', 'n', 'v', 'un']
    Sentence = [
        x.word for x in Sentence if not(
            x.word in Tingyong) and (
            x.flag in ValidFlag)]  # eliminate words in the list of stop words
    f.close()
    return Sentence


'''
Function name:Create_Vector
Task: to convert a word list into a vector
Input:a list of useful words provided by function"Cut_Word"
Output:a vector with 1500 dimension
'''


def Create_Vector(text):
    f = open(r'data\high_frequency.txt')  # the library of frequent word
    Word = f.readlines()
    Word = [x[:-1] for x in Word]
    Vector = [0 for _ in range(1500)]
    for EachWord in text:
        if EachWord in Word:
            Vector[Word.index(EachWord)] += 1
    return Vector


'''
Function name:Main_Process
Task: the entire process to convert a lyric into vector
Input:the path of lyric text
Output:a vector with 1500 dimension
'''


def Main_Process(Path):
    Data = Lyric_Load(Path)
    Sentence = Cut_Word(Data)
    Vector = Create_Vector(Sentence)
    return Vector
