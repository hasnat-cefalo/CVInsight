from typing import List, Optional

from pydantic import BaseModel


class Education(BaseModel):
    degree: Optional[str]
    field_of_study: Optional[str]
    institution: Optional[str]
    location: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]


class Experience(BaseModel):
    position: Optional[str]
    company: Optional[str]
    location: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    responsibilities: Optional[str]


class Contact(BaseModel):
    email: Optional[str]
    phone: Optional[str]
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
