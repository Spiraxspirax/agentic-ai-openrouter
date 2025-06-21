import os
import streamlit as st
from gtts import gTTS
import uuid

from agent_brain import create_agent

# Function to convert text to speech and return audio file path
def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = f"output_{uuid.uuid4()}.mp3"
    tts.save(filename)
    return filename

# Streamlit UI
st.set_page_config(page_title="Agentic AI Chat", page_icon="🧠")
st.title("🤖 Agentic AI Chat with Voice")

# Input box
query = st.text_input("Ask your local AI anything:", placeholder="e.g. What is quantum computing?")

if query:
    with st.spinner("Thinking..."):
        agent = create_agent()
        response = agent.invoke(query)

        # Display response
        st.markdown("### 💬 AI Response")
        st.write(response)

        # Convert response to speech and play
        audio_file = text_to_speech(response)
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/mp3")
