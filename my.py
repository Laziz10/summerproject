#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
from sklearn import datasets
import pickle
from sklearn.ensemble import RandomForestClassifier
#from PIL import Image


pickle_in = open("classifier1.pkl","rb")
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
    Position = st.sidebar.text_input('Position', 1)
    Rate = st.sidebar.text_input('Hourly Rate, USD', 10 )
    Tasks = st.sidebar.text_input('Completed Tasks', 50)
    Appg = st.sidebar.text_input('Total Appearance', 5)
    Timeg = st.sidebar.text_input('Time (AM=0, PM=1)', 0)
    Dayg = st.sidebar.text_input('Day (Weekday=0, Weekend=1)', 0)
    Ctg = st.sidebar.text_input('Category (Furniture=0, Moving=1, Mounting=2)', 1)
    
    data = {'Position': Positiong,
            'Rate': Rateg,
            'Completed Tasks': Tasks,
            'Appearance': Appg,
            'Time': Timeg,
           'Day': Dayg,
           'Category': ctg}
    
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
