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
# Claim Probability
Developed by UNCC students, Dec 2020
""")
html_temp = """
    <div style="background-color:#06c94a;padding:10px">
    <h2 style="color:black;text-align:center;">Probability App </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.sidebar.header('Claim Information:')

def user_input_features():
    Gender = st.sidebar.text_input('Gender (Male=0, Female=1)', 1)
    Date = st.sidebar.text_input('Date', 23 )
    Month = st.sidebar.text_input('Month', 12)
    Type = st.sidebar.text_input('Claimant Type (Indemnity=0, Other=1)', 0)
    Nature = st.sidebar.text_input('Injury Nature (Strain=0, Contusion=1)', 1)
    Body = st.sidebar.text_input('Body (Lower=0, Upper=1)', 1)
    Fatality = st.sidebar.text_input('Fatality (Fatal=0, Non-Fatal=1)', 1)
    Day = st.sidebar.text_input('Age', 15)
    Age = st.sidebar.text_input('Open Days', 23)
    Location = st.sidebar.text_input('Location (East Coast=0, West Coast=1', 0)
    
    data = {'position': Gender,
            'rate': Date,
            'tasks': Month,
            'appear': Type,
            'hired': Nature,
            'Weekend': Body,
           'mounting': Fatality,
           'moving': Day,
           'date': Age,
           'pm': Location}
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Claim Information:')
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
st.subheader('Claim Estimation:')
#st.write(iris.target_names[prediction])
st.write('Below Average: Relax, Happy Holidays!' if prediction==1 else 'Above Average: Contact Dr. Subramaniam!')
st.subheader('Probability in %:')
st.write(prediction_proba)
