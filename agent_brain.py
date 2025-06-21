import os
from langchain_openai import ChatOpenAI

def create_agent():
    return ChatOpenAI(
        temperature=0.7,
        model_name="mistralai/mistral-7b-instruct",
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=os.environ["OPENROUTER_API_KEY"]
    )
