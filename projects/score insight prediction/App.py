import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

# Load the model
model = pkl.load(open('Score_Insight_RanFor.pkl', 'rb'))

# Function to predict credit score
def predict_credit_score(Interest_Rate, Num_Credit_Inquiries, Credit_Mix_Good, Delay_from_due_date, Outstanding_Debt, Payment_of_Min_Amount, Num_Credit_Card, Credit_History_Age):
    x = [[Interest_Rate, Num_Credit_Inquiries, Credit_Mix_Good, Delay_from_due_date, Outstanding_Debt, Payment_of_Min_Amount, Num_Credit_Card, Credit_History_Age]]
    prediction = model.predict(x)
    return prediction



# Main app code
st.header("Score Insight Prediction")
st.sidebar.header("Enter Input Values")

# Input widgets for user input
Interest_Rate_options = [3, 6, 4, 5, 8, 15, 12, 20, 1, 14, 32, 7, 16, 17, 10, 25, 18, 19, 9, 24, 13, 31, 33, 11, 29, 30, 23, 34, 2, 28, 21, 26, 27, 22]
Interest_Rate = st.sidebar.selectbox("Interest Rate", Interest_Rate_options)
Num_Credit_Inquiries = st.sidebar.slider("Number of Credit Inquiries", min_value=0, max_value=15, value=4)

Credit_Mix_Good = st.sidebar.slider("Credit Mix Good", min_value=0, max_value=1, value=0)
Delay_from_due_date = st.sidebar.slider("Delay from Due Date", min_value=0, max_value=55, value=3, key='delay_slider_1')
Outstanding_Debt = st.sidebar.number_input("Outstanding Debt", min_value=0.0, step=1.0, value=502.38)
Payment_of_Min_Amount = st.sidebar.radio("Payment of Minimum Amount", [1, 2, 3])
Num_Credit_Card = st.sidebar.radio("Number of Credit Cards", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
Credit_History_Age = st.sidebar.slider("Credit History Age", min_value=1, max_value=404, value=30)

# Predict Credit Score button
if st.sidebar.button("Predict Credit Score"):
    credit_score = predict_credit_score(Interest_Rate, Num_Credit_Inquiries, Credit_Mix_Good, Delay_from_due_date, Outstanding_Debt, Payment_of_Min_Amount, Num_Credit_Card, Credit_History_Age)
    st.subheader("Predicted Credit Score")
    st.write(f"The predicted credit score is: {credit_score}")

   
