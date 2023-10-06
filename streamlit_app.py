import streamlit as st
import numpy as np

def set_button_style():
    st.markdown(
        """
        <style>
            .stButton > button {
                width: 100px;     /* Width of the square button */
                height: 100px;    /* Height of the square button */
                font-size: 1.2em;
                display: flex;
                justify-content: center;
                align-items: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


# Function to calculate entropy of the sequence
def calculate_entropy(sequence):
    if len(sequence) == 0:
        return 0
    values, counts = np.unique(sequence, return_counts=True)
    probs = counts / len(sequence)
    entropy = -np.sum(probs * np.log2(probs))
    return entropy

# Apply button styling
set_button_style()

# App title
st.title("3x3 Box Entropy Calculator")

# State management for Streamlit
if 'sequence' not in st.session_state:
    st.session_state.sequence = []
if 'entropy_vals' not in st.session_state:
    st.session_state.entropy_vals = []

# Display 3x3 grid and handle box clicks
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.button(f"Box {3*i + j + 1}"):
                st.session_state.sequence.append(3*i + j + 1)
                entropy = calculate_entropy(st.session_state.sequence)
                st.session_state.entropy_vals.append(entropy)

# Display recorded sequence
st.write(f"Sequence: {st.session_state.sequence}")

# Plot the change in entropy
st.line_chart(st.session_state.entropy_vals, use_container_width=True, height=300)

# A button to reset the sequence
if st.button("Reset Sequence"):
    st.session_state.sequence = []
    st.session_state.entropy_vals = []
