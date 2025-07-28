import streamlit as st
import pickle
from PIL import Image
import joblib

# Load model
classifier = joblib.load("model/liver_disease_lgbm.pkl")

# Prediction function
def predict_liver_disease(age, gender, total_bilirubin, direct_bilirubin,alk_phosphate, alamine_aminotransferase,
                          aspartate_aminotransferase, total_proteins, albumin, albumin_globulin_ratio):
    prediction = classifier.predict([[age, gender, total_bilirubin, direct_bilirubin,alk_phosphate, alamine_aminotransferase,
                                      aspartate_aminotransferase, total_proteins, albumin, albumin_globulin_ratio]])
    return int(prediction[0])

# Streamlit page setup
st.set_page_config(page_title="Liver Disease Predictor", page_icon="🩺", layout="centered")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2809/2809733.png", width=120)
st.sidebar.title("About This App")
st.sidebar.markdown("""
This tool uses an AI model trained on ILPD to detect the likelihood of **liver disease**.  
🔬 Designed for educational & diagnostic support.  
🧠 Powered by XGBoost + Streamlit.  
""")

# Header
st.markdown("""
    <div style="background-color:#16a085;padding:15px;border-radius:10px">
    <h2 style="color:white;text-align:center;">🩺 Indian Liver Disease Prediction App</h2>
    <p style="color:white;text-align:center;">AI-powered diagnosis assistant</p>
    </div>
""", unsafe_allow_html=True)

# Form inputs
st.subheader("👤 Enter Patient Details:")

with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, step=1, help="Enter patient's age")
        gender = st.radio("Gender", ("Male", "Female"), help="Select gender")
        gender_code = 1 if gender == "Male" else 0
        total_bilirubin = st.number_input("Total Bilirubin", format="%f", help="e.g., 1.0")
        direct_bilirubin = st.number_input("Direct Bilirubin", format="%f", help="e.g., 1.0")
        alk_phosphate = st.number_input("Alkaline Phosphotase", format="%f", help="e.g., 200")

    with col2:
        alamine_aminotransferase = st.number_input("Alamine Aminotransferase (ALT)", format="%f", help="e.g., 30")
        aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase (AST)", format="%f", help="e.g., 35")
        total_proteins = st.number_input("Total Proteins", format="%f", help="e.g., 6.5")
        albumin = st.number_input("Albumin", format="%f", help="e.g., 3.2")
        albumin_globulin_ratio = st.number_input("A/G Ratio", format="%f", help="e.g., 1.0")

    submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        result = predict_liver_disease(age, gender_code, total_bilirubin, direct_bilirubin,alk_phosphate,
                                       alamine_aminotransferase, aspartate_aminotransferase,
                                       total_proteins, albumin, albumin_globulin_ratio)
        if result == 1:
            st.error("⚠️ **High Risk Detected**: The patient is likely to have liver disease.")
        else:
            st.success("✅ **Low Risk**: The patient is unlikely to have liver disease.")

# About
with st.expander("ℹ️ About"):
    st.markdown("""
    This app was created as a tool to assist in early identification of liver disease risk using 
    clinical data. It uses the Indian Liver Patient Dataset (ILPD) and a machine learning model (XGBoost).
    
    > ⚠️ **Disclaimer:** This tool is for educational and support purposes only. Not a substitute for medical advice.
    """)
