import pandas as pd
import logging as lg
import os


#lg.basicConfig(filename='C:/Users/hares/Desktop/INeuron Internship/Practice/Haresh First Program on Modular coding/log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')
lg.basicConfig(filename='log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')


class DataPrep:
    try:
        def __init__(self):
            pass

        def data_preprocess(self, df):

            for i in df.columns:
                if df[i].dtype == object:
                    df.drop(columns=i, inplace=True)
            lg.info("String columns dropped from Dataframe")


            return df


    except Exception as e:
        print(str(e))
        lg.error(str(e))


    def __str__(self):
        return "this is code for data preprocess"