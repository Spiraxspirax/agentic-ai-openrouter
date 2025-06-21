import os
import streamlit as st
from gtts import gTTS
import io

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer


# Streamlit UI
st.set_page_config(page_title="Nishu's AI Chat", page_icon="🧠")
st.title("Nishu's AI Chat with Voice")

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
