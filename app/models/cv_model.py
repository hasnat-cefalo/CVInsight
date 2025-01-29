from typing import List, Optional

from pydantic import BaseModel


class Education(BaseModel):
    degree: str
    field_of_study: str
    institution: str
    location: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]


class Experience(BaseModel):
    position: str
    company: str
    location: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    responsibilities: Optional[str]


class Contact(BaseModel):
    email: str
    phone: str
    location: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
    website: Optional[str]


class CVModel(BaseModel):
    name: str
    title: Optional[str]
    contact: Contact
    education: Optional[List[Education]]
    experience: Optional[List[Experience]]
    skills: Optional[List[str]]
    skills_from_work_experience: Optional[List[str]]
