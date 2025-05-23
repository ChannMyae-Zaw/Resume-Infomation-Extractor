from langchain_core.tools import tool

@tool
def resume_summary(name: str, education: str, contact: str) -> str:
    summary = f"Resume Summary for {name}:\n"
    summary += f"Name: {name}\nEducation: {education}\nContact: {contact}\n"
    return summary
