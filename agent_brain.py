import os
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Dummy tool that echoes back the input
def echo_tool(input_text: str) -> str:
    return f"You said: {input_text}"

def create_agent():
    llm = ChatOpenAI(
        temperature=0.6,
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        model="openai/gpt-3.5-turbo"
    )

    tools = [
        Tool(
            name="Echo
