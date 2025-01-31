import os
import time
from datetime import datetime

import requests
import streamlit as st

st.set_page_config(
    page_title="CVInsight - AI CV Parser",
    page_icon=":shark:",
    menu_items={
        'Get Help': "mailto:hasnat.abdullah@cefalo.com",
        'Report a bug': "https://github.com/hasnat-cefalo/CVInsight/issues",
        'About': "# Made with ❤️ by Hasnat. Copyright 2025 Cefalo. All rights reserved."
    }
)

model_options = {
    "DeepSeek (Local: R1-1.5B)": "deepseek-r1-1.5b",
    "DeepSeek (Local: R1-7B)": "deepseek-r1-7b",
    "DeepSeek (API)": "deepseek-api",
    "Gemini (Google)": "gemini",
    "Ollama (Local: custom)": "ollama",
    "ChatGPT (OpenAI)": "chatgpt",
}

# Get the backend URL from environment variables
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/api/v1")

# Custom CSS to enhance UI
st.markdown(
    """
    <style>
        .stApp { margin-top: -50px; }
        hr { border: 1px solid #ddd; }
        .scrollable-container { height: 400px; overflow-y: auto; }
    </style>
    """,
    unsafe_allow_html=True,
)


def format_date(date_str):
    """Formats a date string from 'YYYY-MM-DD' to 'Month YYYY'."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %Y")
    except ValueError:
        return date_str  # Return as is if formatting fails


def main():
    st.title("CVInsight - AI CV Parser")
    st.write("Upload a PDF CV and extract structured information using AI.")
    st.write("")
    # File uploader
    uploaded_file = st.file_uploader("Upload a CV (.pdf)", type="pdf", help="Only PDF files are supported.")

    if uploaded_file is not None:
        # Dropdown for selecting the parsing method
        model_type = st.selectbox(
            "Select LLM Model",
            options=list(model_options.keys()),
            index=0,
            help="Choose the LLM model for CV parsing."
        )

        # Parse button
        if st.button("🚀 Parse CV", type="primary"):
            with st.spinner("🔍 Processing CV..."):
                start_time = time.time()
                try:
                    # Prepare the file for sending
                    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                    params = {"model_type": model_options[model_type]}
                    response = requests.post(f"{BACKEND_URL}/parse-cv/", files=files, params=params)
                    execution_time = time.time() - start_time
                    if response.status_code == 200:
                        cv_data = response.json()
                        st.success(f"✅ CV Parsing Successful! (Execution Time: {execution_time:.3f} seconds)")

                        # Create two columns
                        col1, col2 = st.columns([2, 1])  # 2:1 ratio for better visibility

                        # Column 1: Formatted CV
                        with col1:
                            st.subheader("📜 Extracted Information")
                            st.write("---")
                            st.write(f"**👤 Name:** {cv_data.get('name', 'N/A')}")
                            st.write(f"**📧 Title:** {cv_data.get('title', 'N/A')}")

                            # Education
                            if "contact" in cv_data and cv_data["contact"]:
                                contact = cv_data["contact"]
                                st.write("---")
                                st.subheader("📞 Contact")
                                st.write(f"**Email:** {contact.get('email', 'N/A')}")
                                st.write(f"**Phone:** {contact.get('phone', 'N/A')}")
                                st.write(f"**Location:** {contact.get('location', 'N/A')}")
                                st.write(f"**Linkedin:** {contact.get('linkedin', 'N/A')}")
                                st.write(f"**Github:** {contact.get('github', 'N/A')}")
                                st.write(f"**Website:** {contact.get('website', 'N/A')}")

                            # Education
                            if "education" in cv_data and cv_data["education"]:
                                st.write("---")
                                st.subheader("🎓 Education")
                                for edu in cv_data["education"]:
                                    st.write(f"**{edu.get('degree', 'N/A')} in {edu.get('field_of_study', 'N/A')}**")
                                    st.write(f"🏫 {edu.get('institution', 'N/A')}")
                                    st.write(f"📍 {edu.get('location', 'N/A')}")
                                    st.write(
                                        f"🗓️ {format_date(edu.get('start_date', 'N/A'))} - {format_date(edu.get('end_date', 'N/A'))}")
                                    st.markdown("<hr style='border:1px solid #ccc; margin:5px 0;'>",
                                                unsafe_allow_html=True)

                            # Work Experience
                            if "experience" in cv_data and cv_data["experience"]:
                                st.write("---")
                                st.subheader("💼 Work Experience")
                                for exp in cv_data["experience"]:
                                    st.write(f"**{exp.get('position', 'N/A')} at {exp.get('company', 'N/A')}**")
                                    st.write(f"📍 {exp.get('location', 'N/A')}")
                                    st.write(
                                        f"🗓️ {format_date(exp.get('start_date', 'N/A'))} - {format_date(exp.get('end_date', 'N/A'))}")
                                    st.write(f"📝 {exp.get('responsibilities', 'N/A')}")
                                    st.markdown("<hr style='border:1px solid #ccc; margin:5px 0;'>",
                                                unsafe_allow_html=True)

                            # Skills
                            if "skills" in cv_data and cv_data["skills"]:
                                st.write("---")
                                st.subheader("🛠 Skills")
                                st.write(", ".join(cv_data["skills"]))

                            # Skills from work experience
                            if "skills_from_work_experience" in cv_data and cv_data["skills_from_work_experience"]:
                                st.write("---")
                                st.subheader("🛠 Skills from work experience")
                                st.write(", ".join(cv_data["skills_from_work_experience"]))

                        # Column 2: Raw JSON Data
                        with col2:
                            st.subheader("🛠 Raw JSON Data")
                            st.json(cv_data)

                    else:
                        print(response)
                        st.error(f"❌ Error: {response.status_code} - {response.text}")

                except requests.exceptions.RequestException as e:
                    st.error(f"⚠️ Failed to connect to the backend: {e}")
                except Exception as e:
                    st.error(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
