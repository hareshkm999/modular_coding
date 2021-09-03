import pandas as pd
import logging as lg
import os
from sklearn.linear_model import LinearRegression
import pickle

#lg.basicConfig(filename='C:/Users/hares/Desktop/INeuron Internship/Practice/Haresh First Program on Modular coding/log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')
lg.basicConfig(filename='log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')

lr = LinearRegression()


class model_train_test:
    try:
        def __init__(self, X_train, y_train, X_test, y_test):
            self.X_train = X_train
            self.y_train = y_train
            self.X_test = X_test
            self.y_test = y_test

        def model_train_test(self):

            lg.info("Model training started")
            lr.fit(self.X_train, self.y_train)
            lg.info("Model trained done")
            # Writing different model files to file
            with open('model/modelForPrediction.sav', 'wb') as f:
                pickle.dump(lr, f)
            lg.info("model saved")

            accuracy = lr.score(self.X_test, self.y_test)
            lg.info("model tested")
            return accuracy





    except Exception as e:
        print(str(e))
        #lg.error(str(e))


    def __str__(self):
        return "this is code for train test split"