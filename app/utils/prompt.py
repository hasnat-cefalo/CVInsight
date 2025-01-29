prompt = """
You are an expert in parsing and extracting structured information from CVs. Your task is to analyze the provided CV text and extract the following details in a structured JSON format. The JSON must strictly adhere to the schema provided below:

### JSON Schema:
```json
{
  "name": "Full Name of the Candidate",
  "title": "Professional Title or Role",
  "contact": {
    "email": "Email Address",
    "phone": "Phone Number",
    "location": "Location",
    "linkedin": "LinkedIn Profile",
    "github": "GitHub Profile",
    "website": "Personal Website"
  },
  "education": [
    {
      "degree": "Degree Name",
      "field_of_study": "Field of Study",
      "institution": "Institution Name",
      "location": "Location of Institution",
      "start_date": "Start Date (YYYY-MM-DD)",
      "end_date": "End Date (YYYY-MM-DD or 'Present')"
    }
  ],
  "experience": [
    {
      "position": "Job Position",
      "company": "Company Name",
      "location": "Location of Employment",
      "start_date": "Start Date (YYYY-MM-DD)",
      "end_date": "End Date (YYYY-MM-DD or 'Present')",
      "responsibilities": "Key Responsibilities"
    }
  ],
  "skills": ["List of Skills Mentioned in the CV"],
  "skills_from_work_experience": [
    "Top 5 to 10 Skills Derived only from Work Experiences"
  ]
}
"""