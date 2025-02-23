import streamlit as st
import pandas as pd
import joblib

# Load the saved model
loaded_model = joblib.load("aqi_prediction_model.pkl")

# Title of the app
st.title("AQI Prediction App")

# Instructions for users
st.write("Enter values for the independent variables below to predict AQI.")

# Input fields for independent variables
pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0, step=0.1)
pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, step=0.1)
no2 = st.number_input("NO₂ (ppb)", min_value=0.0, step=0.1)
tavg = st.number_input("Average Temperature (°C)", step=0.1)

# Button to make predictions
if st.button("Predict AQI"):
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        "PM2.5": [pm25],
        "PM10": [pm10],
        "NO2": [no2],
        "tavg": [tavg],
    })

    # Make prediction using the loaded model
    predicted_aqi = loaded_model.predict(input_data)

    # Display the prediction
    st.success(f"Predicted AQI: {predicted_aqi[0]:.2f}")
