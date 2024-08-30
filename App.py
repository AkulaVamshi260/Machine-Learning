import numpy as np 
import pandas as pd 
import pickle as pk1
import streamlit as st
 
model=pk1.load(open('MIPML.pk1','rb'))
st.header('Medical Insurance Premium Predictor')


gender=st.selectbox('Choose Gender',['Female','Male'])
smoker=st.selectbox('Are you a smoker ?',['Yes','No'])
region=st.selectbox('Choose Region',['Southeast','Southwest','Northeast','Northwest'])
age=st.slider('Enter Age',5,80)
bmi=st.slider('Enter BMI',5,100)
children=st.slider('Choose No of childrens',0,5)

if gender == 'Female':
    gender = 0
else:
    gender = 1

if smoker == 'No':
    smoker =0
else:
    smoker =1
if region == 'Southeast':
    region =0 
if region == 'Southwest':
    region =1
if region == 'Northeast':
    region =2
else:
    region =3

input_data=(age,gender,bmi,children,smoker,region)
input_data=np.asarray(input_data)
input_data=input_data.reshape(1,-1)
if st.button('Predict'):
    predicted_prem=model.predict(input_data)

    display_string='insurance Premium will be '+str(round(predicted_prem[0],2))+'USD Dollars'
    st.markdown(display_string)
