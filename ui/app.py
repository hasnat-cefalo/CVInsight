import os

import requests
import streamlit as st

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
        # Dropdown for selecting the parsing method
        service_type = st.selectbox(
            "Select Parsing Method",
            options=["nlp", "chatgpt", "deepseek"],  # Matches the ServiceType enum in the backend
            index=0,
            help="Choose the AI model to parse the CV."
        )

        # Send the file to the FastAPI backend
        if st.button("Parse CV"):
            with st.spinner("Parsing CV..."):
                try:
                    # Prepare the file for sending
                    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                    params = {"service_type": service_type}
                    response = requests.post(f"{BACKEND_URL}/parse-cv/", files=files, params=params)

                    if response.status_code == 200:
                        cv_data = response.json()
                        st.success("CV parsed successfully!")
                        st.json(cv_data)  # Display the parsed CV data
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Failed to connect to the backend: {e}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
