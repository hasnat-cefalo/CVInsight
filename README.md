# CVInsight

This is a FastAPI-based AI powered CV parser application that extracts structured data from PDF resumes.

## Features
- Extract text from PDF files.
- Parse CV data (name, email, phone, education, experience, skills) using AI.
- API for uploading and processing CVs.

## Screenshots
Welcome screen
![](/media/images/screen-1.png "Welcome screen")
CV (.pdf) file uploaded
![](/media/images/screen-2.png "CV (.pdf) file uploaded")
Successfully parsed CV
![](/media/images/screen-3.png "Successfully parsed CV")

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
    curl -X POST "http://127.0.0.1:80/api/v1/parse-cv/?service_type=nlp" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@example.pdf"
    ```
  
  - Response

    ```json
    {
      "name": "John Doe",
      "title": "Senior Software Engineer",
      "contact": {
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "location": "New York, USA",
        "linkedin": "https://linkedin.com/in/johndoe",
        "github": "https://github.com/johndoe",
        "website": "https://johndoe.com"
      },
      "education": [
        {
          "degree": "Bachelor of Science",
          "field_of_study": "Computer Science",
          "institution": "University of Example",
          "location": "New York, USA",
          "start_date": "2015-09-01",
          "end_date": "2019-06-01"
        },
        {
          "degree": "Master of Science",
          "field_of_study": "Data Science",
          "institution": "Example Tech University",
          "location": "New York, USA",
          "start_date": "2019-09-01",
          "end_date": "2021-06-01"
        }
      ],
      "experience": [
        {
          "position": "Data Analyst",
          "company": "Tech Solutions Inc.",
          "location": "New York, USA",
          "start_date": "2021-06-01",
          "end_date": "2023-12-01",
          "responsibilities": "Analyzed large datasets to identify trends and improve business decisions."
        },
        {
          "position": "Data Scientist",
          "company": "Innovative Data Co.",
          "location": "Remote",
          "start_date": "2023-12-01",
          "end_date": "Present",
          "responsibilities": "Developed machine learning models for predictive analytics and automation."
        }
      ],
      "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "Data Visualization",
        "Big Data Technologies"
      ],
      "skills_from_work_experience": [
        "Data Analysis",
        "Statistical Modeling",
        "Data Wrangling",
        "Time Series Forecasting"
      ]
    }
    ```

## Testing
Run the unit tests:
```bash
python -m unittest discover tests
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
