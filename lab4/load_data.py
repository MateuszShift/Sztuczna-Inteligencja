import numpy as np
import pandas as pd


def generate_data():
    TRAIN_SAMPLES = 100
    TEST_SAMPLES = 20
    FEATURE_DIM = 5

    X_train = np.random.rand(TRAIN_SAMPLES, FEATURE_DIM)
    y_train = np.random.binomial(1, 0.5, TRAIN_SAMPLES)
    X_test = np.random.rand(TEST_SAMPLES, FEATURE_DIM)
    y_test = np.random.binomial(1, 0.5, TEST_SAMPLES)
    return (X_train, y_train), (X_test, y_test)


def load_titanic():

    data = pd.read_csv("titanic.csv")
    data = data[["Pclass", "Fare", "Parch", "SibSp", "Age", "Sex", "Survived"]] # wybieranie kolumn z danych 
    data = data.dropna().reset_index(drop=True) # usuwanie wierszy z brakującymi danymi
    data["Sex"] = [1 if sex == "female" else 0 for sex in data["Sex"]] # zamiana wartosci w kolumnach na 1 i 0
    test_idx = np.random.choice(range(data.shape[0]), round(0.2*data.shape[0]), replace=False) # wybieranie indeksów do zbioru testowego
    data_test = data.iloc[test_idx, :] # wybieranie danych testowych na podstawie indeksów 
    data_train = data.drop(test_idx, axis=0) # wybieranie danych treningowych na podstawie indeksów 
    X_train = data_train.drop("Survived", axis=1).to_numpy() # wybieranie danych treningowych bez kolumny Survived i zamiana na numpy array 
    y_train = data_train["Survived"].to_numpy() # wybieranie kolumny Survived i zamiana na numpy array 
    X_test = data_test.drop("Survived", axis=1).to_numpy() # wybieranie danych testowych bez kolumny Survived i zamiana na numpy array
    y_test = data_test["Survived"].to_numpy() # wybieranie kolumny Survived i zamiana na numpy array
    return (X_train, y_train), (X_test, y_test) # zwracanie danych treningowych i testowych


