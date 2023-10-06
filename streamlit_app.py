# Import necessary libraries
import streamlit as st

def main():
    # Title of the app
    st.title("Chat Simulation")

    # Store the conversation history in a session state if it doesn't exist
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # Text box for user input
    user_input = st.text_input("You:")

    # Submit button to send the message
    if st.button("Submit"):
        # Append the user's message to the conversation history
        st.session_state.conversation_history.append(f"You: {user_input}")
        
        # Here you can add some logic for generating a response, for now, let's just echo the user's message
        response = f"ChatGPT: I received your message: '{user_input}'."
        st.session_state.conversation_history.append(response)

    # Display the conversation history
    for message in st.session_state.conversation_history:
        st.write(message)

if __name__ == "__main__":
    main()
