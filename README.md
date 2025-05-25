
#------------------- Dataset Download ---------------------
import kagglehub

# Download latest version
path = kagglehub.dataset_download("willianoliveiragibin/healthcare-insurance")

print("Path to dataset files:", path)



# 📊 Insurance Prediction App

A simple and interactive web application built using **Streamlit** that estimates a user's insurance cost based on demographic and health information using a pre-trained **Random Forest Regressor** model (`rfr_model`).

---

## 🚀 Features

- Predicts insurance cost using:
  - Age
  - Gender
  - BMI (Body Mass Index)
  - Number of children
  - Smoking status
- User-friendly sidebar input
- Responsive UI with real-time prediction
- Ensures data privacy (no storage or tracking)

---

## 🧠 Model Info

- **Model type**: Random Forest Regressor (RFR)
- **Library**: `scikit-learn`
- **File**: `rfr_model` (pre-trained and serialized using `joblib`)

---

## 📦 Requirements

Install dependencies via pip:

```bash
pip install -r requirements.txt
```

#### `requirements.txt` (suggested contents):

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## 🛠️ How to Run

1. Clone the repository or download the files.
2. Make sure `rfr_model` (your trained model) is in the same directory.
3. Run the Streamlit app:

```bash
streamlit run app.py
```

> Replace `app.py` with your actual script filename if different.

---

## 📁 File Structure

```
📁 insurance-prediction-app/
├── app.py              # Main Streamlit application
├── rfr_model           # Serialized machine learning model
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ✨ UI Preview

- Sidebar for user input
- Center panel displays:
  - Welcome message
  - Feature explanation
  - Estimated insurance cost after form submission

---

## ⚠️ Note

- Currently supports "Male" and "Female". If "Other" is selected, it defaults to female logic (can be enhanced).
- Ensure the `rfr_model` matches the input format expected in `process_input()`.

---

## 🌐 Live Demo

You can try the app live here 👉 [Insurance Prediction App](https://s8kuiry-insurance-prediction-app-app-ja1vkq.streamlit.app/)

> 🟢 No installation needed — just open the link and start predicting!


---

## 📬 Contact

Have feedback or questions? Open an issue or reach out!
