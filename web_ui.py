import os
import streamlit as st
from agent_brain import create_agent
import asyncio
import edge_tts

# Function: Generate speech from text
async def generate_speech(text, voice="en-US-AriaNeural"):
    communicate = edge_tts.Communicate(text, voice)
    output_file = "output.mp3"
    await communicate.save(output_file)
    return output_file

# Wrapper to call async function from sync Streamlit
def text_to_speech(text):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(generate_speech(text))

# Streamlit App UI
st.set_page_config(page_title
