# CVInsight

This is a FastAPI-based AI powered CV parser application that extracts structured data from PDF resumes.

## Features
- Extract text from PDF files.
- Parse CV data (name, email, phone, education, experience, skills) using AI.
- API for uploading and processing CVs.

## Screenshots
Welcome screen
![](/media/images/screen_1.png "Welcome screen")
Successfully parsed CV
![](/media/images/screen_2.png "Successfully parsed CV")

## Prerequisites
- Python 3.9 or higher
- Docker and Docker Compose (optional, for containerized deployment)


## 1. Clone the Repository
```bash
git clone git@github.com:hasnat-cefalo/CVInsight.git
cd CVInsight
```

## Running the Application

### Option 1: Run with **Docker Compose**
Use Docker Compose to start the service:
```bash
docker-compose up --build
```
UI Link: [http://127.0.0.1:8501](http://127.0.0.1:8501) <br>
API Link: [http://127.0.0.1:8000](http://127.0.0.1:8501)

### Option 2: Run Locally with Python
#### 1. Set Up the Environment
Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
#### 2. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```
UI Link: [http://127.0.0.1:8501](http://127.0.0.1:8501) <br>
API Link: [http://127.0.0.1:8000](http://127.0.0.1:8501)


## API Endpoints

### Parse a CV
- **POST** `/api/v1/parse-cv/`
  - Upload a PDF file to parse the CV.
  - Example request:
    ```bash
    curl -X POST -F "file=@path/to/your/resume.pdf" http://127.0.0.1:80/api/v1/parse-cv/
    ```
  - Response:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "123-456-7890",
      "education": [
        {
          "institution": "University of Example",
          "degree": "Bachelor of Science",
          "field_of_study": "Computer Science",
          "start_date": "2015-09-01",
          "end_date": "2019-05-01"
        }
      ],
      "experience": [
        {
          "company": "Example Corp",
          "position": "Software Engineer",
          "start_date": "2019-06-01",
          "end_date": "2021-12-31",
          "description": "Developed web applications using Python and FastAPI."
        }
      ],
      "skills": ["Python", "FastAPI", "Machine Learning"]
    }
    ```

## Testing
Run the unit tests:
```bash
python -m unittest discover tests
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
