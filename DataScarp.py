import pandas as pd
import logging as lg
import os

#lg.basicConfig(filename='C:/Users/hares/Desktop/INeuron Internship/Practice/Haresh First Program on Modular coding/log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')
lg.basicConfig(filename='log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')


class DataScarp:
    try:
        def __init__(self, path):
            self.path = path

        def data_load(self):
            lg.info("Data Loaded to Dataframe is started")
            df = pd.read_csv(self.path)
            lg.info("Data Loaded to Dataframe is loaeded")

            return df


    except Exception as e:
        print(str(e))
        lg.error(str(e))

    def __str__(self):
        return "this is code for data scrapping"
