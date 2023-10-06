# Importing necessary libraries
import streamlit as st

# Title for the app
st.title("Square Calculator")

# Taking a number input from the user
number = st.number_input("Enter a number", value=1.0)

# Calculating the square and displaying it
st.write(f"The square of {number} is {number**2}")
