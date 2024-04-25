feature = np.arange(X.shape[1]) # tworzymy tablicę z indeksami cech
        if feature_subset is not None: # jeśli feature_subset nie jest puste
            np.random.shuffle(feature) # tasowanie cech
            feature = feature[:feature_subset] # wybieramy tylko tyle cech ile jest w parametrze feature_subset