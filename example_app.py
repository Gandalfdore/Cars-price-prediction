import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from sklearn.ensemble import RandomForestRegressor

st.title('Automobile price calculator')

# some nice image
image_url = 'https://img.freepik.com/premium-vector/car-front-view-bundle-cars-different-configuration-styles-set-modern-automobiles-motor-vehicles-illustration_106796-433.jpg'
st.image(image_url, caption='Courtesy of img.freepik.com', use_column_width=True)

# Load the model from the file
with open('models//simple_random_forest_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# the error
rmse = 2038.26

# define the variable to be inputed
engine_size = st.slider('engine_size', 61, 326, 150)  
curb_weight = st.slider('curb_weight', 1500, 4066, 2000)    
city_mpg = st.slider('city_mpg', 10, 49, 25)    
horsepower = st.slider('horsepower', 48, 262, 120) 
highway_mpg = st.slider('highway_mpg', 13, 54, 25)  

# predict the values
predicted_value = loaded_model.predict([[engine_size, curb_weight, city_mpg, horsepower, highway_mpg]])
print(predicted_value[0],"+-",rmse)

# display them
st.markdown(f'<div style="font-size: 24px; padding: 10px; border: 2px solid #4682B4; border-radius: 5px;">The predicted price is: {predicted_value[0]:.2f} ± {rmse:.2f} [arb.units]</div>', unsafe_allow_html=True)

##############

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12), sharex=True)

# get the original data for illustration purposes
df = pd.read_csv(("data//clean_data.csv"))

# some explanations
st.subheader('Prices of all automobiles')
st.write('Below you can see how your price compares to other vehicles prices and which brands tend to offer a vehicle in your price range.')

# Set the theme to dark mode for Matplotlib
plt.style.use('dark_background')

# Plot the histogram of the prices
sns.histplot(df['price'], bins='auto', edgecolor='black', kde=False, color='blue', ax=ax1)
ax2.set_title('Price Distributions')
ax1.set_ylabel('Price')
ax1.set_ylabel('Frequency')

# Highlight the position on the x-axis corresponding to predicted_value
ax1.axvline(x=predicted_value, color='red', linestyle='--', linewidth=3)

## add a box plot of the brands
sns.boxplot(x='price', y='make', data=df, ax=ax2)
ax2.set_title('Brand vs Price')

# Highlight the position on the x-axis corresponding to predicted_value
ax2.axvline(x=predicted_value, color='red', linestyle='--', linewidth=3)

# Adjust layout
plt.tight_layout()

# Display the plot using Streamlit
st.pyplot(fig)