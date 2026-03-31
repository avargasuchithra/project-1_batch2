import streamlit as st
import joblib
import pandas as pd
import numpy as np

#Load the model and label encoder
model = joblib.load("attrition_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
feature_columns = joblib.load("feature_columns.pkl")
st.title("Employee Attrition Prediction")
#function to get user input for prediction
st.sidebar.header("Employee Details")

def get_user_input():
    inputs={}
    inputs['Age']=st.sidebar.number_input("Age,min_value=18,max_value=65,value=30")
    inputs['MonthlyIncome']=st.sidebar.number_input("Monthly Income",min_value=1000,max_value=200000,value=5000)
    inputs['JobSatisfaction']=st.sidebar.selectbox("JobSatisfaction",options=[1,2,3,4])
    inputs['OverTime']=st.sidebar.selectbox("Over Time",options=["Yes", "No"])
    inputs['DistanceFromHome']=st.sidebar.number_input("Distance From Home",min_value=0,max_value=50,value=10)
get_user_input()