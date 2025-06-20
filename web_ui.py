import streamlit as st
from agent_brain import create_agent

st.set_page_config(page_title="💡 OpenRouter AI Chat", layout="centered")
st.title("🤖 Agentic AI with OpenRouter")
st.markdown("This is a free, hosted AI assistant powered by **OpenRouter + Streamlit**.")

if "llm" not in st.session_state:
    st.session_state.llm = create_agent()

query = st.text_input("Ask your AI something:")

if st.button("Send"):
    if query.strip():
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.llm.invoke(query)
                st.success(response)
            except Exception as e:
                st.error(f"❌ Error: {e}")
