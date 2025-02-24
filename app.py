import streamlit as st
import pandas as pd
import joblib
import streamlit as st
import numpy as np

# Load the saved model
loaded_model = joblib.load("aqi_prediction_model.pkl")

# Title of the app
st.title("AQI Prediction App")


# Instructions for users
st.write("Enter values for the independent variables below to predict AQI.")



# Define ranges for each parameter (customize these based on your data criteria)
pm25_range = (0, 500)      # PM2.5 in µg/m³
pm10_range = (0, 600)      # PM10 in µg/m³
no2_range = (0, 100)       # NO₂ in ppb
co_range = (0, 20)         # CO in ppm
so2_range = (0, 50)        # SO₂ in ppb
o3_range = (0, 150)        # O₃ in ppb
tavg_range = (0, 40)       # Average Temperature in °C 
rh_range = (0, 100)        # Relative Humidity in %
wspd_range = (0, 15)       # Wind Speed in m/s

# Initialize session state for each parameter if not already set
if 'pm25' not in st.session_state:
    st.session_state['pm25'] = 100.0
if 'pm10' not in st.session_state:
    st.session_state['pm10'] = 100.0
if 'NO2' not in st.session_state:
    st.session_state['NO2'] = 30.0
if 'CO' not in st.session_state:
    st.session_state['CO'] = 5.0
if 'SO2' not in st.session_state:
    st.session_state['SO2'] = 5.0
if 'O3' not in st.session_state:
    st.session_state['O3'] = 30.0
if 'tavg' not in st.session_state:
    st.session_state['tavg'] = 15.0
if 'rh' not in st.session_state:
    st.session_state['rh'] = 50.0
if 'wspd' not in st.session_state:
    st.session_state['wspd'] = 5.0


# Function to generate random values for all features based on defined ranges
def generate_random_values():
    st.session_state['pm25'] = np.random.uniform(*pm25_range)
    st.session_state['pm10'] = np.random.uniform(*pm10_range)
    st.session_state['NO2'] = np.random.uniform(*no2_range)
    st.session_state['CO'] = np.random.uniform(*co_range)
    st.session_state['SO2'] = np.random.uniform(*so2_range)
    st.session_state['O3'] = np.random.uniform(*o3_range)
    st.session_state['tavg'] = np.random.uniform(*tavg_range)
    st.session_state['rh'] = np.random.uniform(*rh_range)
    st.session_state['wspd'] = np.random.uniform(*wspd_range)
# Button to trigger random value generation
if st.button("Generate Random Values"):
    generate_random_values()

# Input fields for independent variables
pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0, step=0.1)
pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, step=0.1)
no2 = st.number_input("NO₂ (ppb)", min_value=0.0, step=0.1)
co = st.number_input("CO (ppm)", min_value=0.0, step=0.1)
so2 = st.number_input("SO₂ (ppb)", min_value=0.0, step=0.1)
o3 = st.number_input("O₃ (ppb)", min_value=0.0, step=0.1)
tavg = st.number_input("Average Temperature (°C)", step=0.1)
rh = st.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, step=1.0)
wspd = st.number_input("Wind Speed (m/s)", min_value=0.0, step=0.1)

    
# Button to make predictions
if st.button("Predict AQI"):
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        "PM2.5": [pm25],
        "PM10": [pm10],
        "NO2": [no2],
        "CO": [co],
        "SO2": [so2],
        "O3": [o3],
        "tavg": [tavg],
        "rh": [rh],
        "wspd": [wspd]
    })
    # Make prediction using the loaded model
    predicted_aqi = loaded_model.predict(input_data)

    # Display the prediction
    st.success(f"Predicted AQI: {predicted_aqi[0]:.2f}")




