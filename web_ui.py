import os
import streamlit as st
from gtts import gTTS
import io
from agent_brain import create_agent

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

st.set_page_config(page_title="Nishu AI Chat", page_icon="🧠")
st.title("🤖 Nishu AI Chat with Voice")

query = st.text_input("Ask your local AI anything:", placeholder="e.g. What is quantum computing?")

if query:
    with st.spinner("Thinking..."):
        agent = create_agent()
        response = agent.invoke(query)

        st.markdown("### 💬 AI Response")
        st.write(response)

        # Convert to speech
        audio_buffer = text_to_speech(response)
        st.audio(audio_buffer, format="audio/mp3")
