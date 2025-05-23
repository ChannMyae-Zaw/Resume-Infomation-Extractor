import streamlit as st
import tempfile
import json
import re
import pandas as pd
from llm.chains import resume_prompt_chain
from parsers.dataframe_formatter import parse_analysis_dataframe, parse_summary_dataframe
from utils.pdf_utils import extract_text_from_pdf

st.set_page_config(layout="wide")
uploaded_files = st.file_uploader("Upload PDF Resumes", type="pdf", accept_multiple_files=True)
all_data = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.success(f"Processing: {uploaded_file.name}")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        raw_text = extract_text_from_pdf(tmp_path)
        with st.expander(f"📄 Raw Preview: {uploaded_file.name}"):
            st.text(raw_text[:1000] + "..." if len(raw_text) > 1000 else raw_text)

        response = resume_prompt_chain.invoke({"content": raw_text}).content.strip()
        cleaned_response = re.sub(r"^```(?:json)?\s*|\s*```$", "", response.strip(), flags=re.IGNORECASE)

        try:
            data = json.loads(cleaned_response)
            all_data.append(data)
        except json.JSONDecodeError:
            st.error(f"⚠️ Could not parse JSON for {uploaded_file.name}")
            st.code(response)

    if all_data:
        st.subheader("📊 Combined Education Analysis")
        combined_analysis = pd.concat([parse_analysis_dataframe(d) for d in all_data], ignore_index=True)
        st.dataframe(combined_analysis)

        st.subheader("📝 Summary View")
        combined_summary = pd.concat([parse_summary_dataframe(d) for d in all_data], ignore_index=True)
        st.dataframe(combined_summary)
