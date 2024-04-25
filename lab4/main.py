import numpy as np
from decision_tree import DecisionTree
from random_forest import RandomForest
from load_data import generate_data, load_titanic

def main():
<<<<<<< HEAD
<<<<<<< HEAD
    np.random.seed(123) 
=======
    np.random.seed(123)
>>>>>>> 6c2a2b0 (Dodanie kolejnej części)
=======
    np.random.seed(123) 
>>>>>>> efadf93 (bagging and feature selection changes)

    train_data, test_data = load_titanic()

    dt = DecisionTree({"depth": 14})
    dt.train(*train_data)
    dt.evaluate(*train_data)
    dt.evaluate(*test_data)

<<<<<<< HEAD
<<<<<<< HEAD
    rf = RandomForest({"ntrees": 100, "feature_subset": 2, "depth": 14})
    rf.train(*train_data) 
    
=======
    rf = RandomForest({"ntrees": 10, "feature_subset": 2, "depth": 14})
    rf.train(*train_data)
>>>>>>> 6c2a2b0 (Dodanie kolejnej części)
=======
    rf = RandomForest({"ntrees": 100, "feature_subset": 2, "depth": 14})
    rf.train(*train_data) 
>>>>>>> efadf93 (bagging and feature selection changes)
    rf.evaluate(*train_data)
    rf.evaluate(*test_data)

if __name__=="__main__":
    main()