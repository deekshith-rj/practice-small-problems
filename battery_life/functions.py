import pandas as pd


def read_train():
    train = pd.read_csv('trainingdata.txt', header=None, names=['time_charged', 'time_used'])
    return train
