import pandas as pd
import streamlit as st
import joblib

model = joblib.load('model.pkl')

st.title('walmart sales predictor')

#'Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI','Unemployment'

Store = st.number_input('Store', min_value = 1, max_value =45)
Holiday_Flag = st.selectbox('Holiday Flag', options = [1, 0])
Temperature = st.number_input('Temperature', min_value = -2.0, max_value = 100.0)
Fuel_Price = st.number_input('Fuel Price', min_value = 0.0, max_value = 10.0)
CPI = st.number_input('CPi', min_value = 0.0, max_value = 500.0)
Unemployment = st.number_input('Unemployment', min_value = 0 )

if st.button("Predict Sales"):
    input_data = pd.DataFrame ({
        'Store': [Store],
        'Holiday_Flag': [Holiday_Flag],
        'Temperature': [Temperature],
        'Fuel_Price': [Fuel_Price],
        'CPI': [CPI],
        'Unemployment': [Unemployment]
    })
       
    Prediction = model.predict(input_data)
    st.success(f"The Predicted Sales For store {Store} is ${Prediction[0]}")