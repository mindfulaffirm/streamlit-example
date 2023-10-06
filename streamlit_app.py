import streamlit as st
import numpy as np

# Function to calculate entropy of the sequence
def calculate_entropy(sequence):
    # If sequence is empty, return 0
    if len(sequence) == 0:
        return 0

    # Count frequency of each box click
    values, counts = np.unique(sequence, return_counts=True)
    probs = counts / len(sequence)
    entropy = -np.sum(probs * np.log2(probs))
    return entropy

# App title
st.title("3x3 Box Entropy Calculator")

# State management for Streamlit (to remember the sequence across reruns)
if 'sequence' not in st.session_state:
    st.session_state.sequence = []

# Display 3x3 grid and handle box clicks
for i in range(3):
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        if st.button(f"Box {3*i + 1}"):
            st.session_state.sequence.append(3*i + 1)
    with col2:
        if st.button(f"Box {3*i + 2}"):
            st.session_state.sequence.append(3*i + 2)
    with col3:
        if st.button(f"Box {3*i + 3}"):
            st.session_state.sequence.append(3*i + 3)

# Display recorded sequence
st.write(f"Sequence: {st.session_state.sequence}")

# Calculate and display entropy
entropy = calculate_entropy(st.session_state.sequence)
st.write(f"Entropy: {entropy}")

# A button to reset the sequence if needed
if st.button("Reset Sequence"):
    st.session_state.sequence = []
