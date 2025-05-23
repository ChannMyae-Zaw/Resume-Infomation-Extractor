from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

openrouter_llm = ChatOpenAI(
    model="deepseek/deepseek-r1:free",
    temperature=0,
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

google_llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key="AIzaSyDaqs8EUSEa0FH9bUyI4_0P2mhDG5-C7ok",
    temperature=0
)