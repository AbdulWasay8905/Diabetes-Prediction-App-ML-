# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Load dataset
df = pd.read_csv("diabetes.csv")

# Load trained model
classifier = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🩺 Diabetes Prediction App")

st.write("Move the sliders to input patient details and predict diabetes:")

# Create sliders with dynamic min/max from dataset
pregnancies = st.slider("Pregnancies", int(df["Pregnancies"].min()), int(df["Pregnancies"].max()), int(df["Pregnancies"].median()))
glucose = st.slider("Glucose Level", int(df["Glucose"].min()), int(df["Glucose"].max()), int(df["Glucose"].median()))
blood_pressure = st.slider("Blood Pressure", int(df["BloodPressure"].min()), int(df["BloodPressure"].max()), int(df["BloodPressure"].median()))
skin_thickness = st.slider("Skin Thickness", int(df["SkinThickness"].min()), int(df["SkinThickness"].max()), int(df["SkinThickness"].median()))
insulin = st.slider("Insulin", int(df["Insulin"].min()), int(df["Insulin"].max()), int(df["Insulin"].median()))
bmi = st.slider("BMI", float(df["BMI"].min()), float(df["BMI"].max()), float(df["BMI"].median()))
dpf = st.slider("Diabetes Pedigree Function", float(df["DiabetesPedigreeFunction"].min()), float(df["DiabetesPedigreeFunction"].max()), float(df["DiabetesPedigreeFunction"].median()))
age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()), int(df["Age"].median()))

# Prediction button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    input_data_reshaped=input_data.reshape(1,-1)
    std_data=scaler.transform(input_data_reshaped)
    prediction = classifier.predict(std_data)

    if prediction[0] == 0:
        st.success("✅ The person is unlikely to have Diabetes.")

    else:
        st.error("⚠️ The person is likely to have Diabetes.")        


