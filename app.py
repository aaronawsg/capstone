import os
import streamlit as st
import joblib
import numpy as np
import pandas as pd

#df = pd.read_csv("Global_Economic_Data_Cleaned.csv")
COUNTRIES = ["Australia", "Canada", "China", "India", "Russia", "USA"]



# Load the saved sales regression model
@st.cache_resource
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, 'economics.pkl')
    return joblib.load(model_path)

model = load_model()

st.title("🤖 Economics Analysis ML Predictor")


# Input fields
val1 = st.number_input("Literacy Rate (%)", value=94.35)
val2 = st.number_input("Education Expenditure as % of GDP", value=4.94)
val3 = st.number_input("Healthcare Expenditure per Capita (USD)", value=5434.0)
val4 = st.number_input("Doctor-to-Patient Ratio", value=3.53)
val5 = st.number_input("Labor Force Participation Rate (%)", value=69.23)
val6 = st.number_input("Unemployment Rate (%)", value=4.75)
val7 = st.number_input("Renewable Energy Share (%)", value=23.0)
val8 = st.number_input("Poverty Rate (%)", value=9.99)
#val9 = st.text_input("Country", value="Australia")
val9 = st.selectbox("Choose a country", COUNTRIES)

if st.button("Predict"):
    # 1. Arrange inputs into a dictionary mapping to your exact original dataset column names
    input_dict = {
        "Literacy Rate (%)": [val1],
        "Education Expenditure as % of GDP": [val2],
        "Healthcare Expenditure per Capita (USD)": [val3],
        "Doctor-to-Patient Ratio": [val4],
        "Labor Force Participation Rate (%)": [val5],
        "Unemployment Rate (%)": [val6],
        "Renewable Energy Share (%)": [val7],
        "Poverty Rate (%)": [val8],
        "Country": [val9]
    }

    # 2. Convert the dictionary into a pandas DataFrame
    input_df = pd.DataFrame(input_dict)
    
    # 3. Pass the DataFrame to the model instead of the numpy array
    prediction = model.predict(input_df)
    
    #st.success(f"Prediction: {prediction[0]} GDP per capita (in USD)")
    st.success(f"Predicted GDP per capita: USD {prediction[0]:,.0f}")
