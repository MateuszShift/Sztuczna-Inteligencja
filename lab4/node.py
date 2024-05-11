import copy
import random
import numpy as np


class Node: # klasa reprezentująca węzeł drzewa decyzyjnego 
    def __init__(self):
        self.left_child = None 
        self.right_child = None
        self.feature_idx = None # indeks cechy
        self.feature_value = None
        self.node_prediction = None # przewidywana wartość węzła

    def gini_best_score(self, y, possible_splits): # funkcja obliczająca najlepszy podział danych na podstawie indeksu Giniego
        best_gain = -np.inf
        best_idx = 0
        
        n_total = y.shape[0]  # liczba wszystkich danych w zbiorze
        


        # TODO find position of best data split
        for idx in possible_splits: 
            left_y = y[:idx+1] 
            right_y = y[idx+1:]  
            
            total_left = left_y.shape[0] 
            pos_left = np.sum(left_y) 
            neg_left = total_left - pos_left 
            
            total_right = right_y.shape[0] 
            pos_right = np.sum(right_y)
            neg_right = total_right - pos_right
            
            gini_left = 1 - (pos_left / total_left) ** 2 - (neg_left / total_left) ** 2 
            gini_right = 1 - (pos_right / total_right) ** 2 - (neg_right / total_right) ** 2 
            
            gain = 1 - (total_left / n_total) * gini_left - (total_right / n_total) * gini_right 

            if gain > best_gain:
                best_gain = gain
                best_idx = idx
            
        return best_idx, best_gain

    def split_data(self, X, y, idx, val): # funkcja dzieląca dane na podstawie indeksu i wartości
        left_mask = X[:, idx] < val # maska dla lewej części danych 
        return (X[left_mask], y[left_mask]), (X[~left_mask], y[~left_mask]) # zwraca dane podzielone na lewą i prawą część

    def find_possible_splits(self, data): # funkcja znajdująca możliwe punkty podziału danych
        possible_split_points = []
        for idx in range(data.shape[0] - 1): # dla każdego indeksu w danych
            if data[idx] != data[idx + 1]: # jeśli dane na indeksie idx i idx+1 są różne
                possible_split_points.append(idx) # dodajemy indeks do możliwych punktów podziału
        return possible_split_points # zwracamy możliwe punkty podziału

    def find_best_split(self, X, y, feature_subset): # funkcja znajdująca najlepszy podział danych
        best_gain = -np.inf
        best_split = None
        # X to dane, y to etykiety, feature_subset to liczba cech, które chcemy wybrać
        # TODO implement feature selection 
        
        
        if feature_subset is None: 
            feature = [i for i in range(X.shape[1])] 
        else:  
            feature = random.sample(range(X.shape[1]), min(feature_subset, X.shape[1]))
        
        
        
        for d in feature:
            order = np.argsort(X[:, d]) 
            y_sorted = y[order]
            possible_splits = self.find_possible_splits(X[order, d]) 
            idx, value = self.gini_best_score(y_sorted, possible_splits) 
            if value > best_gain: 
                best_gain = value 
                best_split = (d, [idx, idx + 1]) 



    def find_possible_splits(self, data): # funkcja znajdująca możliwe punkty podziału danych
        possible_split_points = []
        for idx in range(data.shape[0] - 1): # dla każdego indeksu w danych
            if data[idx] != data[idx + 1]: # jeśli dane na indeksie idx i idx+1 są różne
                possible_split_points.append(idx) # dodajemy indeks do możliwych punktów podziału
        return possible_split_points # zwracamy możliwe punkty podziału

    def find_best_split(self, X, y, feature_subset): # funkcja znajdująca najlepszy podział danych
        best_gain = -np.inf
        best_split = None
        # X to dane, y to etykiety, feature_subset to liczba cech, które chcemy wybrać
        # TODO implement feature selection 
        
        
        if feature_subset is None: 
            feature = [i for i in range(X.shape[1])] 
        else:  
            feature = random.sample(range(X.shape[1]), min(feature_subset, X.shape[1]))
        
    def predict(self, x):
        if self.feature_idx is None:
            return self.node_prediction
        if x[self.feature_idx] < self.feature_value:
            return self.left_child.predict(x)
        else:
            return self.right_child.predict(x)

    def train(self, X, y, params):

        self.node_prediction = np.mean(y)
        if X.shape[0] == 1 or self.node_prediction == 0 or self.node_prediction == 1:
            return True

        self.feature_idx, self.feature_value = self.find_best_split(X, y, params["feature_subset"])
        if self.feature_idx is None:
            return True

        (X_left, y_left), (X_right, y_right) = self.split_data(X, y, self.feature_idx, self.feature_value)

        if X_left.shape[0] == 0 or X_right.shape[0] == 0:
            self.feature_idx = None
            return True

        # max tree depth
        if params["depth"] is not None:
            params["depth"] -= 1
        if params["depth"] == 0:
            self.feature_idx = None
            return True

        # create new nodes
        self.left_child, self.right_child = Node(), Node()
        self.left_child.train(X_left, y_left, copy.deepcopy(params))
        self.right_child.train(X_right, y_right, copy.deepcopy(params))
