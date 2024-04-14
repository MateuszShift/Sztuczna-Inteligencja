import pandas as pd

def get_small():
    knapsack = pd.read_csv('/Users/macmat/Desktop/4 sem/Sztuczna inteligencja/lab2/knapsack-small.csv')
    return knapsack, 10

def get_big():
    knapsack = pd.read_csv('/Users/macmat/Desktop/4 sem/Sztuczna inteligencja/lab2/knapsack-big.csv')
    return knapsack, 6404180
