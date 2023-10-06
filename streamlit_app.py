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
