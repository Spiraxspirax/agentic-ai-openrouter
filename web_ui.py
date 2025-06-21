import os
import streamlit as st
from agent_brain import create_agent
import asyncio
import edge_tts

# Text-to-speech with edge-tts
async def generate_speech(text, voice="en-US-AriaNeural"):
    communicate = edge_tts.Communicate(text, voice)
    output_file = "output.mp3"
    await communicate.save(output_file)
    return output_file

def text_to_speech(text):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(generate_speech(text))

# Streamlit UI
st.set_page_config(page_title="Agentic AI Chat", page_icon="🧠")
st.title("🤖 Agentic AI Chat with Voice")

query = st.text_input("Ask your local AI anything:")

if query:
    with st.spinner("Thinking..."):
        agent = create_agent()
        response = agent.invoke(query)

        st.markdown("### 💬 AI Response")
        st.write(response)

     audio_path = text_to_speech(str(response))
        with open(audio_path, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")
