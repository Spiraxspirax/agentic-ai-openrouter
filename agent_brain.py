from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
import os

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
            name="Echo Tool",
            func=echo_tool,
            description="Repeats the user's input."
        )
    ]

    return initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
