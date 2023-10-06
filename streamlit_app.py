import streamlit as st
import openai

# OpenAI API key
API_KEY = "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"

# OpenAI settings
openai.api_key = API_KEY

def chatGPT(query):
    response = openai.Completion.create(
        engine="davinci",
        prompt=query,
        max_tokens=150,
        n=1,
        stop=". ",
        temperature=0.7
    )
    return response.choices[0].text.strip()

st.title("Learning Buddy")

# Display buttons and handle their functionality
if st.button('START'):
    prompt = ("Clear all the past memory. Pretend You are me, and I am you, chatGPT. "
              "Keep asking me questions after I answer. The topic is about learning Python programming. "
              "Start with some greetings and an easy question. remember to encourage me along the way. "
              "keep your text short. not more than 15 words")
    response = chatGPT(prompt)
    st.write(f"**Learning Buddy:** {response}")

if st.button('Too difficult!'):
    prompt = "Too difficult"
    response = chatGPT(prompt)
    st.write(f"**Learning Buddy:** {response}")

if st.button('Too easy!'):
    prompt = "Too easy."
    response = chatGPT(prompt)
    st.write(f"**Learning Buddy:** {response}")

# Chat input
query = st.text_input('Continue your conversation...')
if st.button('Chat'):
    if query:
        response = chatGPT(query)
        st.write(f"**Me:** {query}")
        st.write(f"**Learning Buddy:** {response}")
