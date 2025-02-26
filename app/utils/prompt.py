prompt = """
I have extracted text from a pdf formatted resume. Please organize all the relevant information and provide a structured JSON output with the following fields:

Desired JSON format:
{
  "name": "Full Name of the Candidate",
  "title": "Latest Professional Title or Role",
  "contact": {
    "email": "Email Address",
    "phone": "Phone Number",
    "location": "Candidate's Location/address",
    "linkedin": "LinkedIn Profile link",
    "github": "GitHub/gitlab/bitbucket Profile link",
    "other_links": ["other profile links"]
  },
  "education": [
    {
      "degree": "Degree Name",
      "field_of_study": "Field of Study",
      "institution": "Institution Name",
      "location": "Location of Institution",
      "start_date": "Start Date (YYYY-MM-DD)",
      "end_date": "End Date (YYYY-MM-DD or 'Present')",
      "result": "Result (if available)"
    }
  ],
  "experience": [
    {
      "position": "Job Position",
      "company": "Company Name",
      "location": "Location of Employment",
      "start_date": "Start Date (YYYY-MM-DD)",
      "end_date": "End Date (YYYY-MM-DD or 'Present')",
      "responsibilities": "Responsibilities or descriptions"
    }
  ],
  "projects": [
    {
      "title": "Project Title",
      "description": "Project Description",
      "start_date": "Start Date (YYYY-MM-DD)",
      "end_date": "End Date (YYYY-MM-DD or 'Present')",
      "technologies_used": ["List of Technologies Used"]
    }
  ],
  "certifications": [
    {
      "name": "Certification Name",
      "issuing_organization": "Issuing Organization",
      "issue_date": "Issue Date (YYYY-MM-DD)",
      "expiration_date": "Expiration Date (YYYY-MM-DD or 'Present')",
      "credential_id": "Credential ID"
    }
  ],
  "skills": ["List of Skills Mentioned in the CV"],
  "skills_from_work_experience": [
    "Maximum Top 10 Skills Derived only from Work Experiences"
  ]
}

Use the exact words from the provided CV text. Do not add or summarize or hallucinate anything. If a field is missing, leave it as null.
"""