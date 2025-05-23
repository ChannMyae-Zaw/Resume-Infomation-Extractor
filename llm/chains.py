from langchain_core.prompts import ChatPromptTemplate
from llm.models import google_llm

resume_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
    "You are a resume parser. Extract and return the following information "
    "as valid JSON with this structure:\n\n"
    "{{\n"
    '  "name": "Full name",\n'
    '  "education": [\n'
    "    {{\n"
    '      "institution": "University name",\n'
    '      "degree": "Degree name",\n'
    '      "gpa": "GPA if present"\n'
    "    }}, ...\n"
    "  ],\n"
    '  "contact": {{\n'
    '    "phone": "Phone number",\n'
    '    "email": "Email address"\n'
    "  }}\n"
    "}}\n\n"
    "Only output valid JSON. DO NOT include any markdown, code fences, or extra text. DO NOT include any other explanation or formatting. "
    "If some fields are missing, use null or an empty string."),
        ("human", "This is the resume: {content}"),
    ]
)

resume_prompt_chain = resume_prompt | google_llm
