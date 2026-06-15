import base64

import streamlit as st
import pickle
import numpy as np

import base64

# Function to add GIF background
def add_bg_from_local(gif_file):
    with open(gif_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    page_bg_img = f"""
    <style>
    .stApp {{
    background-image: url("data:image/gif;base64,{encoded}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

add_bg_from_local("heart.gif")

st.markdown("""
<style>

/* Labels like Age, Sex, Cholesterol */
label {
    color: #00eaff !important;
    font-weight: bold;
    font-size: 16px;
}

/* Input boxes */
div[data-baseweb="input"] > div {
    background-color: rgba(255,255,255,0.85) !important;
    border-radius: 10px;
}

/* Dropdown boxes */
div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.85) !important;
    border-radius: 10px;
}

/* Input text */
input {
    color: #000000 !important;
    font-weight: bold;
    font-size: 25px;
}

/* Dropdown text */
div[data-baseweb="select"] span {
    color: #000000 !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("heart_disease_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

st.title("")
st.markdown(
    "<h1 style='color:#ff4d6d;'>❤️ Heart Disease Prediction System</h1>",
    unsafe_allow_html=True
)
st.markdown(
"<p style='color:white; font-size:35px; font-weight:bold;'>Enter patient health details to predict heart disease risk.</p>",
unsafe_allow_html=True
)

# User inputs
age = st.number_input("Age")
sex = st.selectbox("Sex",["Male","Female"])
cp = st.selectbox("Chest Pain Type",[0,1,2,3])
bp = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fast = st.selectbox("Fasting Blood Sugar",[0,1])
ecg = st.selectbox("Resting ECG",[0,1,2])
hr = st.number_input("Max Heart Rate")
angina = st.selectbox("Exercise Angina",[0,1])
oldpeak = st.number_input("Oldpeak")
slope = st.selectbox("ST Slope",[0,1,2])

# Convert sex
if sex == "Male":
    sex = 1
else:
    sex = 0


# Prediction button
if st.button("Predict"):

    # Collect user data
    data = np.array([[age, sex, cp, bp, chol, fast, ecg, hr, angina, oldpeak, slope]])

    # Scale the data
    data = scaler.transform(data)

    # Make prediction
    prediction = model.predict(data)

    # Get probability
    probability = model.predict_proba(data)
    risk = probability[0][1] * 100

    # Display risk percentage
    st.markdown(
        f"<h3 style='color:#ff4d6d; text-shadow:0px 0px 10px #ff4d6d;'>❤️ Heart Disease Risk: {risk:.2f}%</h3>",
        unsafe_allow_html=True
    )

    # Progress bar
    st.progress(int(risk))

    # Result message
    if prediction[0] == 1:
        st.markdown(
            "<h1 style='color:#ff4d6d; text-shadow:0px 0px 15px #ff4d6d;'>⚠️ Patient Has Heart Disease Risk</h1>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h1 style='color:#00ff9c; text-shadow:0px 0px 15px #00ff9c;'>✅ Patient is Healthy</h1>",
            unsafe_allow_html=True
        )