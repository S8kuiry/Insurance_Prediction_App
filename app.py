import streamlit as st 
import numpy as np
import joblib
import pandas as pd

# Load model
model = joblib.load('rfr_model')

# Configure page
st.set_page_config(page_title="Insurance Prediction App", layout="centered", initial_sidebar_state="expanded")

# ----------- functions -------------

def process_input(age, sex, bmi, children, smoker):
    sex_encoded = 1 if sex == "Male" else 0
    smoker_encoded = 1 if smoker == "Yes" else 0
    data = pd.DataFrame({
        "age": [age],
        "sex": [sex_encoded],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker_encoded]
    })
    return data

def prection_model(data):
    prediction = model.predict(data)
    return prediction

# ----------- sidebar -------------

st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            width: 300px !important;
        }
        section[data-testid="stSidebar"][aria-expanded="false"] {
            width: 0px !important;
        }
        .stButton>button {
            width: 100%;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1 style='text-align:center;'>⏳ Info Section</h1>", unsafe_allow_html=True)
    st.info("Fill in the details to get an insurance cost estimate.")
    name = st.text_input("🧑 Enter Your Name :")
    age = st.number_input("🎂 Enter Age :", step=1)
    sex = st.selectbox("⚥ Select Gender :", ["Male", "Female", "Other"])
    bmi = st.slider("📏 Select BMI", 10.0, 40.0, step=0.1)
    children = st.number_input("👶 Number of Children :", value=0, step=1)
    smoker = st.selectbox("🚬 Are you a smoker? :", ["Yes", "No"])
    submit = st.button("🚀 Submit")

# ----------- main section -------------

st.markdown("<h1 style='text-align:center;margin-top:-60px;'>📊 Insurance Prediction App</h1>", unsafe_allow_html=True)
st.write("Welcome to the **Insurance Cost Predictor App**. This tool helps estimate your insurance cost based on basic demographic and lifestyle inputs.")

st.markdown("""
### 📌 What this app considers:
- **Age**
- **Gender**
- **Body Mass Index (BMI)**
- **Number of Children**
- **Smoker status**

> 💡 Your data remains private and is not stored.
""")

# ----------- logic -------------

if name and age and sex and bmi and children is not None and smoker:
    if submit:
        data = process_input(age=age, sex=sex, bmi=bmi, children=children, smoker=smoker)
        value = int(prection_model(data=data))
        st.balloons()
        st.success(f"🎉 {name}, your estimated insurance cost is: **${value:,}** 💰")
else:
    st.warning("🌟 Please fill out all the required fields in the sidebar to get your prediction.")

