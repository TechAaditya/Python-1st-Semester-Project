import streamlit as st
import numpy as np
import pandas as pd
import joblib

# -----------------------------------------------------------------------------
# TITLE & IMAGE
# -----------------------------------------------------------------------------
st.title("AQI Prediction App")
st.write("This app predicts the Air Quality Index (AQI) based on input values for pollutants and meteorological parameters.")

# Display AQI scale image
st.image("aqi_scale_image.jpg", caption="Air Quality Index Scale", use_column_width=True)

# -----------------------------------------------------------------------------
# DEFINE PARAMETER RANGES (adjust these based on your data/criteria)
# -----------------------------------------------------------------------------
pm25_range = (0, 500)      # PM2.5, in µg/m³
pm10_range = (0, 600)      # PM10, in µg/m³
no2_range = (0, 100)       # NO₂, in ppb
co_range = (0, 20)         # CO, in ppm
so2_range = (0, 50)        # SO₂, in ppb
o3_range = (0, 150)        # O₃, in ppb
tavg_range = (0, 40)       # Average Temperature in °C
rh_range = (0, 100)        # Relative Humidity in %
wspd_range = (0, 15)       # Wind Speed in m/s

# -----------------------------------------------------------------------------
# INITIALIZE SESSION STATE FOR EACH PARAMETER
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# FUNCTION TO GENERATE RANDOM VALUES FOR PARAMETERS
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# INPUT FIELDS FOR THE PARAMETERS (populated with session state values)
# -----------------------------------------------------------------------------
pm25_val = st.number_input("PM2.5 (µg/m³)", value=float(st.session_state['pm25']))
pm10_val = st.number_input("PM10 (µg/m³)", value=float(st.session_state['pm10']))
no2_val = st.number_input("NO₂ (ppb)", value=float(st.session_state['NO2']))
co_val = st.number_input("CO (ppm)", value=float(st.session_state['CO']))
so2_val = st.number_input("SO₂ (ppb)", value=float(st.session_state['SO2']))
o3_val = st.number_input("O₃ (ppb)", value=float(st.session_state['O3']))
tavg_val = st.number_input("Average Temperature (°C)", value=float(st.session_state['tavg']))
rh_val = st.number_input("Relative Humidity (%)", value=float(st.session_state['rh']))
wspd_val = st.number_input("Wind Speed (m/s)", value=float(st.session_state['wspd']))

# -----------------------------------------------------------------------------
# FUNCTION TO DETERMINE AQI CATEGORY BASED ON PREDICTED VALUE
# -----------------------------------------------------------------------------
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# -----------------------------------------------------------------------------
# PREDICTION FUNCTIONALITY
# -----------------------------------------------------------------------------
if st.button("Predict AQI"):
    # Create a DataFrame from the input values
    input_data = pd.DataFrame({
        "PM2.5": [pm25_val],
        "PM10": [pm10_val],
        "NO2": [no2_val],
        "CO": [co_val],
        "SO2": [so2_val],
        "O3": [o3_val],
        "tavg": [tavg_val],
        "rh": [rh_val],
        "wspd": [wspd_val]
    })
    
    # Load the pre-trained AQI prediction model
    loaded_model = joblib.load("aqi_prediction_model.pkl")
    
    # Make the prediction
    prediction = loaded_model.predict(input_data)[0]
    
    # Determine AQI category based on prediction
    aqi_category = get_aqi_category(prediction)
    
    # Display the prediction result and category
    st.success(f"Predicted AQI: {prediction:.2f}")
    st.info(f"AQI Category: {aqi_category}")
