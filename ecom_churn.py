import pandas as pd
import streamlit as st
import numpy as np
import joblib


preprocessor = joblib.load("col_encoder.pkl")
model = joblib.load("model_cus.pkl")

st.title("Customer Churn Prediction App")
st.write("This app is made to predict if a particular customer will churn or not, based on particylar set of features")
st.header("please enter the following information for prediction purpose")

Age = st.number_input("Age", min_value=18, max_value=100, value=20)
Gender = st.selectbox("Gender", ["Male", "Female", "Other"])
Country = st.selectbox("Country", ['France', 'UK', 'Canada', 'USA', 'Japan', 'Germany', 'India','Australia'])
City = st.selectbox("City", ['Marseille', 'Manchester', 'Vancouver', 'New York', 'Tokyo',
       'Berlin', 'Houston', 'Glasgow', 'Munich', 'Phoenix', 'Paris',
       'Ottawa', 'Bangalore', 'Yokohama', 'Los Angeles', 'Sydney',
       'Nagoya', 'Nice', 'Chicago', 'Toulouse', 'Brisbane', 'Montreal',
       'Melbourne', 'Hyderabad', 'Leeds', 'Birmingham', 'Hamburg',
       'Calgary', 'London', 'Cologne', 'Toronto', 'Adelaide', 'Lyon',
       'Kyoto', 'Osaka', 'Chennai', 'Perth', 'Delhi', 'Mumbai',
       'Frankfurt'])
Membership_Years = st.number_input("Membership Years", min_value=0, max_value=30, value=2)
Login_Frequency = st.number_input("Login Frequency", min_value=0, max_value=30, value=5)
Session_Duration_Avg = st.number_input("Session_Duration_Avg", min_value=0, max_value=50, value=5)
Pages_Per_Session = st.number_input("Pages Per Session", min_value=0, max_value=30, value=5)
Cart_Abandonment_Rate = st.number_input("Cart Abandonment Rate", min_value=0.0, max_value=100.0, value=20.0)
Total_Purchases = st.number_input("Total Purchases", min_value=0, max_value=100, value=20)
Average_Order_Value = st.number_input("Average Order Value", min_value=0, max_value=500, value=20)
Days_Since_Last_Purchase = st.number_input("Days Since Last_Purchase", min_value=0, max_value=80, value=5)
Discount_Usage_Rate = st.number_input("Discount Usage Rate", min_value=0.0, max_value=100.0, value=20.0)
Mobile_App_Usage = st.number_input("Mobile App Usage", min_value=0.0, max_value=100.0, value=20.0)
Lifetime_Value = st.number_input("Lifetime Value", min_value=0, max_value=50000, value=200)
Credit_Balance = st.number_input("Credit Balance", min_value=0, max_value=50000, value=200)


# Column Mapping

columns = {
    'Age': Age,
    'Gender': Gender,
    'Country': Country,
    'City': City,
    'Membership_Years': Membership_Years,
    'Login_Frequency': Login_Frequency,
    'Session_Duration_Avg': Session_Duration_Avg,
    'Pages_Per_Session': Pages_Per_Session,
    'Cart_Abandonment_Rate': Cart_Abandonment_Rate,
    'Total_Purchases': Total_Purchases,
    'Average_Order_Value': Average_Order_Value,
    'Days_Since_Last_Purchase': Days_Since_Last_Purchase,
    'Discount_Usage_Rate': Discount_Usage_Rate,
    'Mobile_App_Usage': Mobile_App_Usage,
    'Lifetime_Value': Lifetime_Value,
    'Credit_Balance': Credit_Balance
}


def data_prep(columns):
    input_data = pd.DataFrame([columns])
    data = preprocessor.transform(input_data)
    prediction = model.predict(data)
    return prediction


if st.button("predict"):
    prediction = data_prep(columns)
    if prediction == 0:
        st.error("This customer is likely to churn")
    else:
        st.success("This customer wont churn")

else:
    st.info("Please click the button to predict")



