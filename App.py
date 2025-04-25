import streamlit as st
import numpy as np
import pickle

# Load the model
with open('random_forest_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Cancer Prediction Web App By Ankita")
st.write("🔍 This app uses a Random Forest Classifier to predict type of cancer.")

# Collect user input
age = st.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", options=["Female", "Male"])
tumor_size = st.number_input("Tumor Size (in cm)", min_value=0.0, value=2.5)
location = st.selectbox("Tumor Location", options=["Frontal", "Occipital", "Parietal", "Temporal"])  # Update as per your values
histology = st.selectbox("Histology Type", options=["Astrocytoma", "Glioblastoma", "Medulloblastoma", "Meningioma"])         # Update as per your values
stage = st.selectbox("Cancer Stage", options={0: "Stage 0", 1: "Stage 1", 2: "Stage 2", 3: "Stage 3", 4: "Stage 4"})

symptom_1 = st.selectbox("Symptom 1", options=["Headache", "Nausea", "Fatigue", "Dizziness"])
symptom_2 = st.selectbox("Symptom 2", options=["Headache", "Nausea", "Fatigue", "Dizziness"])
symptom_3 = st.selectbox("Symptom 3", options=["Headache", "Nausea", "Fatigue", "Dizziness"])
radiation = st.selectbox("Radiation Treatment Received", options=["Yes", "No"])
surgery = st.selectbox("Surgery Performed", options=["Yes", "No"])
chemo = st.selectbox("Chemotherapy Received", options=["Yes", "No"])

survival_rate = st.number_input("Survival Rate (%)", min_value=0.0, max_value=100.0, value=75.0)
tumor_growth_rate = st.number_input("Tumor Growth Rate", min_value=0.0, value=1.2)

family_history = st.selectbox("Family History of Cancer", options=["Yes", "No"])
mri_result = st.selectbox("MRI Result Abnormality", options=["Yes", "No"])
follow_up = st.selectbox("Follow-Up Required?", options=["Yes", "No"])

# Button to predict
if st.button("Predict Follow-up Requirement"):
    input_data = np.array([[
        age,
        0 if gender == "Female" else 1,
        tumor_size,
        location.index(location),  # Convert location to index
        histology.index(histology),  # Convert histology to index
        stage, 
        symptom_1.index(symptom_1),  # Convert symptom_1 to index
        symptom_2.index(symptom_2),  # Convert symptom_2 to index
        symptom_3.index(symptom_3),  # Convert symptom_3 to index
        1 if radiation == "Yes" else 0,
        1 if surgery == "Yes" else 0,
        1 if chemo == "Yes" else 0,
        survival_rate,
        tumor_growth_rate,
        1 if family_history == "Yes" else 0,
        1 if mri_result == "Yes" else 0, 
        1 if follow_up == "Yes" else 0
    ]])

    # Prediction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🔴 Malignant Cancer !!!")
    else:
        st.success("🟢 Benign Cancer !!!")
