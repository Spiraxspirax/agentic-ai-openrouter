import os
import streamlit as st
import asyncio
import edge_tts

async def generate_speech(text, voice="en-US-AriaNeural"):
    communicate = edge_tts.Communicate(text, voice)
    output_file = "output.mp3"
    await communicate.save(output_file)
    return output_file

def text_to_speech(text):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(generate_speech(text))


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
