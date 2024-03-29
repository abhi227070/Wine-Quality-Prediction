# Wine Quality Prediction

## Table of Contents
1. [Project Overview](#project-overview)
2. [Use Cases](#use-cases)
3. [Running the Project](#running-the-project)
4. [Streamlit Code](#streamlit-code)
5. [Technologies Used](#technologies-used)
6. [Acknowledgements](#acknowledgements)
7. [Screenshots](#screenshots)
8. [License](#license)

## Project Overview

The Wine Quality Prediction project employs machine learning algorithms to assess the quality of wine. It's a multiclass classification project where various parameters of wine, such as acidity, sulfur oxide content, pH, density, and others, are measured to predict the quality of the wine. By analyzing these parameters, the model can classify the wine into different quality categories.

## Use Cases

1. **Wine Industry**: Wineries and vineyards can utilize this model to evaluate the quality of their wine batches. By inputting the parameters of each batch, they can assess its quality and make informed decisions regarding production and marketing strategies.

2. **Quality Control**: Wine distributors and retailers can employ this model for quality control purposes. They can verify the quality of the wines they receive from suppliers before stocking them, ensuring consistent quality for their customers.

3. **Wine Enthusiasts**: Wine enthusiasts and consumers can use this tool to evaluate the quality of wines they intend to purchase. By inputting the parameters provided on wine labels, they can gain insights into the expected quality of the wine.

## Running the Project

To run the project locally:

1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Run the application using Streamlit by executing `streamlit run app.py`.
5. Access the application in your web browser at `http://localhost:8501`.

## Streamlit Code

```python
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
```
## Technologies Used

Python
Machine Learning (scikit-learn)
Streamlit

## Acknowledgements

This project utilizes machine learning algorithms for wine quality prediction and Streamlit for building the user interface. It aims to provide a convenient tool for evaluating wine quality based on its characteristics.

## Screenshots



## License

This project is licensed under the terms of the MIT license. See the [LICENSE] file for details.
