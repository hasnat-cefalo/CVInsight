import os
import requests
import streamlit as st
from datetime import datetime

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

    # File uploader
    uploaded_file = st.file_uploader("Upload a CV (.pdf)", type="pdf", help="Only PDF files are supported.")

    if uploaded_file is not None:
        # Dropdown for selecting the parsing method
        service_type = st.selectbox(
            "Select AI Model",
            options=["nlp", "chatgpt", "deepseek"],
            index=0,
            help="Choose the AI model for CV parsing."
        )

        # Parse button
        if st.button("🚀 Parse CV"):
            with st.spinner("🔍 Processing CV..."):
                try:
                    # Prepare the file for sending
                    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                    params = {"service_type": service_type}
                    response = requests.post(f"{BACKEND_URL}/parse-cv/", files=files, params=params)

                    if response.status_code == 200:
                        cv_data = response.json()
                        st.success("✅ CV Parsing Successful!")

                        # Create two columns
                        col1, col2 = st.columns([2, 1])  # 2:1 ratio for better visibility

                        # Column 1: Formatted CV
                        with col1:
                            st.subheader("📜 Extracted Information")
                            st.write(f"**👤 Name:** {cv_data.get('name', 'N/A')}")
                            st.write(f"**📧 Email:** {cv_data.get('email', 'N/A')}")
                            st.write(f"**📞 Phone:** {cv_data.get('phone', 'N/A')}")
                            st.write("---")

                            # Education
                            if "education" in cv_data and cv_data["education"]:
                                st.subheader("🎓 Education")
                                for edu in cv_data["education"]:
                                    st.write(f"**{edu.get('degree', 'N/A')} in {edu.get('field_of_study', 'N/A')}**")
                                    st.write(f"🏫 {edu.get('institution', 'N/A')}")
                                    st.write(f"🗓️ {format_date(edu.get('start_date', 'N/A'))} - {format_date(edu.get('end_date', 'N/A'))}")
                                    st.write("---")

                            # Work Experience
                            if "experience" in cv_data and cv_data["experience"]:
                                st.subheader("💼 Work Experience")
                                for exp in cv_data["experience"]:
                                    st.write(f"**{exp.get('position', 'N/A')} at {exp.get('company', 'N/A')}**")
                                    st.write(f"🗓️ {format_date(exp.get('start_date', 'N/A'))} - {format_date(exp.get('end_date', 'N/A'))}")
                                    st.write(f"📝 {exp.get('description', 'N/A')}")
                                    st.write("---")

                            # Skills
                            if "skills" in cv_data and cv_data["skills"]:
                                st.subheader("🛠 Skills")
                                st.write(", ".join(cv_data["skills"]))

                        # Column 2: Raw JSON Data
                        with col2:
                            st.subheader("🛠 Raw JSON Data")
                            st.json(cv_data)

                    else:
                        st.error(f"❌ Error: {response.status_code} - {response.text}")

                except requests.exceptions.RequestException as e:
                    st.error(f"⚠️ Failed to connect to the backend: {e}")
                except Exception as e:
                    st.error(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()