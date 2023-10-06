import streamlit as st

# Initializing session state variables if they don't exist
if 'button1_color' not in st.session_state:
    st.session_state.button1_color = 'primary'
if 'button2_color' not in st.session_state:
    st.session_state.button2_color = 'primary'

# If Button 1 is clicked, toggle its color
if st.button('Button 1', key='btn1', on_click=lambda: setattr(st.session_state, 'button1_color', 'danger' if st.session_state.button1_color == 'primary' else 'primary'), color=st.session_state.button1_color):
    st.write('Button 1 clicked!')

# If Button 2 is clicked, toggle its color
if st.button('Button 2', key='btn2', on_click=lambda: setattr(st.session_state, 'button2_color', 'danger' if st.session_state.button2_color == 'primary' else 'primary'), color=st.session_state.button2_color):
    st.write('Button 2 clicked!')
