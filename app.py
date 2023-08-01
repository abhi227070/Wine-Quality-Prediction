import streamlit as st
import pickle
import pandas as pd
import numpy as np

df = pd.read_csv("winequality-red.csv")
model = pickle.load(open("wine_quality_detection.pkl","rb"))

st.title("Wine Quality Prediction")

st.write("Please Fill the Following Parameter:")

c1,c2 = st.columns(2)

with c1:
    
    fixed = st.number_input("Fixed Acidity:")
    volatile = st.number_input("Volatile Acidity:")
    citric = st.number_input("Citric Acid:")
    sugar = st.number_input("Residual Sugar:")
    chlorides = st.number_input("Chloride Quantity:")
    free = st.number_input("Free Sulfur Dioxide:")
with c2:
    total = st.number_input("Total Sulfur Dioxide:")
    density = st.number_input("Density:")
    ph = st.number_input("PH:")
    sulphate = st.number_input("Sulphate Quantity:")
    alcohol = st.number_input("Alcohol Quantity:")

if st.button("Predict"):
    
    input_data=(fixed,volatile,citric,sugar,chlorides,free,total,density,ph,sulphate,alcohol)
    input_data=np.asarray(input_data)
    input_data=input_data.reshape(1,-1)
    prediction=model.predict(input_data)
    if prediction[0]==1:
        st.success("Wine quality is good.")
    else:
        st.success("Wine quality is not good.")