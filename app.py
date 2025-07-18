import pandas as pd
import pickle as pk
import streamlit as st

#To Load the trained model pipeline (which includes the encoder)
model = pk.load(open('C:/Users/TANMAYI/Desktop/python/House_prediction_model.pkl','rb'))

#To Load location list for dropdown
data = pd.read_csv('Cleaned_data.csv')

# Title
st.header('Bangalore House Predictor')

# User Inputs
loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter Total Sqft', min_value=100.0)
beds = st.number_input('Enter No of Bedrooms', min_value=1.0, step=1.0)
bath = st.number_input('Enter No of Bathrooms', min_value=1.0, step=1.0)
balc = st.number_input('Enter No of Balconies', min_value=0.0, step=1.0)

# Prediction button
if st.button("Predict Price"):
    # Now Build input dataframe
    input_df = pd.DataFrame([[loc, sqft, bath, balc, beds]],
                            columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

    try:
        # Predict using the model
        output = model.predict(input_df)
        predicted_price = output[0] * 100000  # To Convert lakhs to rupees
        st.success(f'Predicted Price: ₹{predicted_price:,.2f}')
    except Exception as e:
        st.error(f"Prediction failed: {e}")
