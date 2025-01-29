import streamlit as st
import requests
import os

# Get the backend URL from environment variables
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/api/v1")

def main():
    # Custom CSS to reduce the gap before the title
    st.markdown(
        """
        <style>
        .stApp {
            margin-top: -50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("CVInsight")
    st.subheader("AI powered CV Parser")
    st.write("")
    st.write("Upload a PDF file to parse the CV.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:

        # Send the file to the FastAPI backend
        if st.button("Parse CV"):
            # Prepare the file for sending
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            response = requests.post(f"{BACKEND_URL}/parse-cv/", files=files)

            if response.status_code == 200:
                cv_data = response.json()
                st.success("CV parsed successfully!")
                st.json(cv_data)  # Display the parsed CV data
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()