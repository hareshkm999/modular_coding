import pandas as pd
import logging as lg
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle


#lg.basicConfig(filename='C:/Users/hares/Desktop/INeuron Internship/Practice/Haresh First Program on Modular coding/log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')
lg.basicConfig(filename='log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')
scalar = StandardScaler()


class train_test_standardise:
    try:
        def __init__(self, X, y):
            self.X = X
            self.y = y

        def Split(self):
            x = scalar.fit_transform(self.X)
            y1 = self.y.values
            lg.info("train test split started")
            X_train, X_test, y_train, y_test = train_test_split(x, y1, test_size=0.3, random_state=455)
            with open('model/modelsandardScalar.sav', 'wb') as f:
                pickle.dump(scalar, f)
            lg.info("train test split finished")


            return X_train, X_test, y_train, y_test



    except Exception as e:
        lg.error(str(e))

    def __str__(self):
        return "this is code for train test split"