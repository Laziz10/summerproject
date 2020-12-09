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
# TASK RABBIT APP
Developed by "Team 49", UNCC, 2020
""")
html_temp = """
    <div style="background-color:#12e65c;padding:10px">
    <h2 style="color:white;text-align:center;">Will a Tasker be hired? </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.sidebar.header('Tasker Information')

def user_input_features():
    Positiong = st.sidebar.text_input('Position', 1)
    Rateg = st.sidebar.text_input('Hourly Rate, USD', 10 )
    Tasks = st.sidebar.text_input('Completed Tasks', 50)
    Appg = st.sidebar.text_input('Total Appearance', 5)
    Hiredg = st.sidebar.text_input('Completed Tasks', 0)
    Weekg = st.sidebar.text_input('Weekend', 0)
    Dateg = st.sidebar.text_input('Date', 0)
    Dayg = st.sidebar.text_input('AM or PM', 0)
    Mounting = st.sidebar.text_input('Mounting', 1)
    Moving = st.sidebar.text_input('Moving', 1)
    
    data = {'position': Positiong,
            'rate': Rateg,
            'tasks': Tasks,
            'appear': Appg,
            'hired': Hiredg,
            'Weekend': Weekg,
            'date': Dateg;
           'pm': Dayg,
           'mounting': Mounting,
           'moving': Moving}
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Tasker Information')
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
st.subheader('Result')
#st.write(iris.target_names[prediction])
st.write('Hired' if prediction==0 else 'Not Hired')
st.subheader('Prediction Probability')
st.write(prediction_proba)
# In[ ]:
