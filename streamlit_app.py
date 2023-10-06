import streamlit as st
import openai

# Set up OpenAI GPT-3 API
openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_gpt3_response(prompt):
    """Function to get GPT-3's response to a given prompt."""
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()

def main():
    st.title("Chat Simulation with GPT-3")

    # Store the conversation history in a session state if it doesn't exist
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # Text box for user input
    user_input = st.text_input("You:")

    # Submit button to send the message
    if st.button("Submit"):
        # Append the user's message to the conversation history
        st.session_state.conversation_history.append(f"You: {user_input}")

        # Get GPT-3's response
        gpt3_response = get_gpt3_response(user_input)
        st.session_state.conversation_history.append(f"ChatGPT: {gpt3_response}")

    # Display the conversation history
    for message in st.session_state.conversation_history:
        st.write(message)

if __name__ == "__main__":
    main()
``
