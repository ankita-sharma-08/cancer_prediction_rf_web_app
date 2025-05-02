# Cancer Prediction Web App

Enter the patient detail in the following Link , this predict the tumor type
  https://cancer-detection-by.streamlit.app/

# Overview:
The Cancer Prediction Web App is an interactive tool designed to assist healthcare professionals and patients in predicting the type of cancer based on various clinical and demographic factors. Utilizing a Random Forest Classifier, this app leverages machine learning to analyze user inputs and provide insights into the likelihood of benign or malignant tumors.

# Key Features:

User -Friendly Interface: The app features an intuitive design that allows users to easily input relevant data, including age, gender, tumor characteristics, and treatment history.

Data Input Options: Users can provide information on:

Demographics: Age and gender.

Tumor Characteristics: Size, location, histology type, and stage of cancer.

Symptoms: Users can select from common symptoms associated with tumors.

Treatment History: Options to indicate whether radiation treatment, surgery, or chemotherapy has been received.

Survival and Growth Rates: Users can input estimated survival rates and tumor growth rates.

Family History and MRI Results: Options to indicate family history of cancer and any abnormalities found in MRI results.

Predictive Analysis: Once the user inputs the necessary data, the app utilizes a trained Random Forest model to predict the likelihood of the tumor being malignant or benign.

## Results Display: The app provides immediate feedback on the prediction, indicating whether the tumor is likely to be malignant (🔴) or benign (🟢), along with a confidence level based on the input data.

Technological Stack:

Backend: The app is powered by a Random Forest Classifier model, which has been trained on historical cancer data to ensure accurate predictions.

Frontend: Built using Streamlit, a powerful framework for creating web applications in Python, allowing for rapid development and deployment.
Use Cases:

Healthcare Professionals: Doctors and oncologists can use this tool to support their clinical decision-making process.

Patients: Individuals seeking to understand their health conditions can use the app to gain insights into their symptoms and treatment options.

## Disclaimer: This app is intended for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
