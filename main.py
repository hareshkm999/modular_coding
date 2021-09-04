from wsgiref import simple_server
from flask import Flask, request, render_template
import pickle
import time
import logging as lg
from DataScarp import DataScarp
from model_train import *
from data_preprocess import *
from train_test_standardise import *
from model_train import *
#import json
#import numpy as np
"""
*****************************************************************************
*
* filename:       main.py
* version:        1.0
* author:         HARISH
* creation date:  2-feb-2021
*
* change history:
*
* who             when           version  change (include bug# if apply)
* ----------      -----------    -------  ------------------------------
* HARISH          23-JAN-2021    1.0      initial creation
*
*
* description:    flask main file to run application
*
****************************************************************************
"""
#lg.basicConfig(filename='C:/Users/hares/Desktop/INeuron Internship/Practice/Haresh First Program on Modular coding/log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')
lg.basicConfig(filename='log/app.log', level=lg.INFO, format='%(asctime)s %(message)s')

app = Flask(__name__)



@app.route('/')
def index_page():
    """
    * method: index_page
    * description: method to call index html page
    * return: index.html
    *
    * who             when           version  change (include bug# if apply)
    * ----------      -----------    -------  ------------------------------
    * HARISH          23-JAN-2021    1.0      initial creation
    *
    * Parameters
    *   None
    """
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            air_temperature = float(request.form['air_temperature'])
            rotational_speed = float(request.form['rotational_speed'])
            torque = float(request.form['torque'])
            wear = float(request.form['wear'])
            failure = float(request.form['failure'])
            twf = float(request.form['twf'])
            hdf = float(request.form['hdf'])
            pwf = float(request.form['pwf'])
            osf = float(request.form['osf'])
            rnf = float(request.form['rnf'])
            lg.info("prediction started")
            with open('model/modelForPrediction.sav', 'rb') as f:
                loaded_model = pickle.load(f)
                prediction = str(list(loaded_model.predict([[air_temperature, rotational_speed, torque, wear, failure, twf, hdf, pwf, osf, rnf]])))
            with open('Result/Prediction.txt', 'a') as f:
                localtime = time.localtime(time.time())
                timestring = time.strftime('%Y/%m/%d - %H:%M:%S')
                f.writelines('Local current time : %s     ' % timestring)
                f.writelines(prediction)
            lg.info("prediction done")


            #return render_template('result.html', prediction=prediction)
            return "prediction results captured, prediction is   : " + str(prediction)
        else:
            return render_template('index.html')
    except Exception as e:
        lg.error(str(e))


@app.route("/train", methods=['POST'])
def train():
    try:
        if request.method == 'POST':
            #path = 'C:/Users/hares/Desktop/INeuron Internship/Practice/Haresh First Program on Modular coding/data/ai4i2020.csv'
            path = 'data/ai4i2020.csv'

            # Data load
            data = DataScarp(path)
            df = data.data_load()

            # Data preprocess
            data_scrap = DataPrep()
            df = data_scrap.data_preprocess(df)

            # Removing ID Column
            df.drop(columns='UDI', inplace=True)

            # preparing for X and y
            X = df.drop(columns='Process temperature [K]')
            y = df['Process temperature [K]']

            # spliting dataset as train and test
            tts = train_test_standardise(X, y)
            X_train, X_test, y_train, y_test = tts.Split()

            # training dataset
            model_train = model_train_test(X_train, y_train, X_test, y_test)
            accuracy = model_train.model_train_test()
            print(accuracy)

            return "accuracy of model is  : " + str(accuracy)
        else:
            return render_template('index.html')
    except Exception as e:
        lg.error(str(e))


if __name__ == "__main__":
    app.run(debug=True)
    #host = '0.0.0.0'
    #port = 5026
    #httpd = simple_server.make_server(host, port, app)
    #httpd.serve_forever()
