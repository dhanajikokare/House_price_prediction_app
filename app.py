import streamlit as st

import pandas as pd
import numpy as np

import joblib

#Load Model
model = joblib.load('model/house_price_model.pkl')


st.title("House Price Prediction App")

st.write("Enter the house details to eliminate" "the expected house price")


l=['Area', 'Bedrooms', 'Bathrooms', 'Floors', 'YearBuilt',
       'Location_Downtown', 'Location_Rural', 'Location_Suburban',
       'Location_Urban', 'Condition_Excellent', 'Condition_Fair',
       'Condition_Good', 'Condition_Poor', 'Garage_No', 'Garage_Yes']

# Input fields for user to enter house details
area = st.number_input("Area (in square feet)", min_value=100, max_value=10000, value=1000)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=1)
year_built = st.number_input("Year Built", min_value=1900, max_value=2024, value=2000)
location_downtown = st.checkbox("Location: Downtown")
location_rural = st.checkbox("Location: Rural")
location_suburban = st.checkbox("Location: Suburban")
location_urban = st.checkbox("Location: Urban")
condition_excellent = st.checkbox("Condition: Excellent")
condition_fair = st.checkbox("Condition: Fair")
condition_good = st.checkbox("Condition: Good")
condition_poor = st.checkbox("Condition: Poor")
garage_no = st.checkbox("Garage: No")
garage_yes = st.checkbox("Garage: Yes")


if st.button("Predict Price"):

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'Area': [area],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Floors': [floors],
        'YearBuilt': [year_built],
        'Location_Downtown': [int(location_downtown)],
        'Location_Rural': [int(location_rural)],
        'Location_Suburban': [int(location_suburban)],
        'Location_Urban': [int(location_urban)],
        'Condition_Excellent': [int(condition_excellent)],
        'Condition_Fair': [int(condition_fair)],
        'Condition_Good': [int(condition_good)],
        'Condition_Poor': [int(condition_poor)],
        'Garage_No': [int(garage_no)],
        'Garage_Yes': [int(garage_yes)]
    })  

    # Ensure the input data has the same columns as the model expects
    input_data = input_data.reindex(columns=    l, fill_value=0)

    # Make prediction
    prediction = model.predict(input_data)

    st.success(f"The predicted house price is: ${prediction[0][0]:,.2f}")

