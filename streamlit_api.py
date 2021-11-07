#from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import streamlit as st


pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def get_note_authenticity(variance2,skewness2,curtosis2,entropy2):

    prediction=classifier.predict([[variance2,skewness2,curtosis2,entropy2]])
    return prediction

def main():
    st.title('Note Authenticator')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=get_note_authenticity(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

