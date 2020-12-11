#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import pandas as pd
from sklearn import datasets
import pickle
from sklearn.ensemble import RandomForestClassifier
#from PIL import Image


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)



#img=Image.open("example.jpeg")
#st.image(img, width=300)

st.write("""
# TASK RABBIT
Developed by "TEAM 49", UNCC, 2020
""")
html_temp = """
    <div style="background-color:#06c94a;padding:10px">
    <h2 style="color:black;text-align:center;">Probability App </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.sidebar.header('Tasker Information')

def user_input_features():
    Positiong = st.sidebar.text_input('Position', 1)
    Rateg = st.sidebar.text_input('Hourly Rate, USD', 30 )
    Tasks = st.sidebar.text_input('Completed Tasks', 0)
    Appg = st.sidebar.text_input('Total Appearance', 10)
    Hiredg = st.sidebar.text_input('Total Hired', 10)
    Dateg = st.sidebar.text_input('Date', 1)
    Weekg = st.sidebar.text_input('Day (Weekday=0, Weekday=1)', 0)
    Dayg = st.sidebar.text_input('Time (AM=0, PM=1)', 0)
    Mounting = st.sidebar.text_input('Task Type (Mounting=1)', 0)
    Moving = st.sidebar.text_input('Task Type (Moving=1)', 1)
    
    data = {'position': Positiong,
            'rate': Rateg,
            'tasks': Tasks,
            'appear': Appg,
            'hired': Hiredg,
            'date': Dateg,
            'Weekend': Weekg,
            'pm': Dayg,
           'mounting': Mounting,
           'moving': Moving}
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Tasker Information:')
st.write(df)

#iris = datasets.load_iris()
#X = iris.data
#Y = iris.target
#clf = RandomForestClassifier()
#clf.fit(X, Y)
prediction = classifier.predict(df)
prediction_proba =classifier.predict_proba(df)
#st.subheader('Class labels and their corresponding index number')
#st.write(iris.target_names)
st.subheader('Prediction:')
#st.write(iris.target_names[prediction])
st.write('Congrats, Hired!' if prediction==1 else 'Sorry, Not Hired :(')
st.subheader('Probability in %:')
st.write(prediction_proba)
