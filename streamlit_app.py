import streamlit as st
import requests

# Set up Azure OpenAI API endpoint and key
AZURE_ENDPOINT = 'https://nie-gpt.openai.azure.com/openai/deployments/GPT_4/chat/completions?api-version=2023-06-01-preview&api-key=250783a2a3ed4cbe93dd0d7d2c443144'  # Replace with your endpoint
AZURE_API_KEY = '250783a2a3ed4cbe93dd0d7d2c443144'  # Replace with your key

headers = {
    "Content-Type": "application/json"
}

def get_gpt3_response_from_azure(prompt):
    """Function to get GPT-3's response from Azure's OpenAI service."""
    data = {
    "model": "gpt-4",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "How are you doing today?"
        }
    ],
    "temperature": 0.7,
    "top_p": 1,
    "max_tokens": 256
}
    response = requests.post(AZURE_ENDPOINT, headers=headers, json=data)
    response_json = response.json()

    # Extract and return the response text from the JSON response (adjust as per Azure's response structure)
    return response_json['choices'][0]['message']['content']

def main():
    st.title("Chat Simulation with Azure OpenAI GPT-3")

    # Store the conversation history in a session state if it doesn't exist
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # Text box for user input
    user_input = st.text_input("You:")

    # Submit button to send the message
    if st.button("Submit"):
        # Append the user's message to the conversation history
        st.session_state.conversation_history.append(f"You: {user_input}")
        
        # Get GPT-3's response from Azure
        gpt3_response = get_gpt3_response_from_azure(user_input)
        st.session_state.conversation_history.append(f"ChatGPT: {gpt3_response}")

    # Display the conversation history
    for message in st.session_state.conversation_history:
        st.write(message)

if __name__ == "__main__":
    main()
