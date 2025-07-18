
# 🏡 Bangalore House Price Prediction App

This project is a simple **machine learning-based web application** that predicts house prices in Bangalore using user input features like location, square footage, bedrooms, bathrooms, and balconies.

The app is built with **Streamlit** and uses a trained ML model stored as a `.pkl` file.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit web app script |
| `Cleaned_data.csv` | Dataset used for the location dropdown |
| `House_prediction_model.pkl` | Pre-trained machine learning model (pickle file) |
| `README.md` | This documentation file |

---

## 🚀 How to Run the App

### 1. 📦 Install Dependencies

Make sure Python is installed, then install required libraries:
```bash
pip install pandas streamlit scikit-learn
```

### 2. ▶️ Launch the Streamlit App
Run this command from your project folder:
```bash
streamlit run app.py
```

---

## 🧠 How It Works

- Loads a trained machine learning model (`.pkl`) using `pickle`.
- Loads cleaned housing data from a CSV for dropdown selection of locations.
- Takes user input via UI (square feet, bedrooms, bathrooms, balconies).
- Constructs a DataFrame with the same feature structure as the trained model.
- Predicts house price and shows output in rupees (× ₹100000 multiplier).

---

## 📌 Input Fields

- 📍 Location (dropdown)
- 📐 Total Square Feet
- 🛏 Bedrooms
- 🛁 Bathrooms
- 🚪 Balconies

---

## 💻 Code Overview (`app.py`)

```python
import pandas as pd
import pickle as pk
import streamlit as st

# Load the trained model
model = pk.load(open('C:/Users/TANMAYI/Desktop/python/House_prediction_model.pkl','rb'))

# App UI
st.header('Bangalore House Predictor')
data = pd.read_csv('Cleaned_data.csv')

# User input
loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter Total Sqft')
beds = st.number_input('Enter No of Bedrooms')
bath = st.number_input('Enter No of Bathrooms')
balc = st.number_input('Enter No of Balconies')

# Prepare input for model
input = pd.DataFrame([[loc, sqft, bath, balc, beds]], 
                     columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

# Prediction
if st.button("Predict Price"):
    output = model.predict(input)
    st.success('Price of the House is ₹ {:.2f}'.format(output[0] * 100000))
```

---

## 📷 Example Output

> 🟢 *Price of the House is ₹ 57,00,000.00*

---

## 📌 Notes

- Ensure that the model was trained on data matching the same column structure.
- `location` feature must be processed inside the model (e.g., via one-hot encoding during training).
- You can modify the paths if you're working on a different system.

---

## 🔮 Future Add-ons

- Add map-based location picker
- Use ensemble models (Random Forest, XGBoost)
- Add deployment support (Streamlit Cloud, Heroku)

---

## 📜 License

This project is for educational purposes. You are free to modify or reuse it.
