from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger


app=Flask(__name__)
Swagger(app)

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=['GET'])
def get_note_authenticity():
    """ Lets find out the fake notes
    This is using docstrings for specifications
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true

    responses:
        200:
            description: The output values

    """
    variance2=request.args.get('variance')
    skewness2=request.args.get('skewness')
    curtosis2=request.args.get('curtosis')
    entropy2=request.args.get('entropy')
    prediction=classifier.predict([[variance2,skewness2,curtosis2,entropy2]])
    return "The predicted value is"+str(prediction)

@app.route('/predict_file',methods=['POST'])
def get_note_file():
    """ Lets find out the fake notes
    This is using docstrings for specifications
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true

    responses:
        200:
            description: The output values

    """
    df_test=pd.read_csv(request.files.get('file'))
    prediction=classifier.predict(df_test)
    return str(list(prediction))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)