from flask import Flask,request
import pandas as pd
import numpy as np
import pickle


app=Flask(__name__)

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def get_note_authenticity():
    variance2=request.args.get('variance')
    skewness2=request.args.get('skewness')
    curtosis2=request.args.get('curtosis')
    entropy2=request.args.get('entropy')
    prediction=classifier.predict([[variance2,skewness2,curtosis2,entropy2]])
    return "The predicted value is"+str(prediction)

@app.route('/predict-file',methods=['POST'])
def get_note_file():
    df_test=pd.read_csv(request.files.get('file'))
    prediction=classifier.predict(df_test)
    return str(list(prediction))


if __name__=='__main__':
    app.run()