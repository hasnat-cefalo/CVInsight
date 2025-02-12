from typing import List, Optional
from pydantic import BaseModel, Field


class Education(BaseModel):
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    institution: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    result: Optional[str] = None


class Experience(BaseModel):
    position: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    responsibilities: Optional[str] = None


class Project(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    technologies_used: List[str] = Field(default_factory=list)


class Certification(BaseModel):
    name: Optional[str] = None
    issuing_organization: Optional[str] = None
    issue_date: Optional[str] = None
    expiration_date: Optional[str] = None
    credential_id: Optional[str] = None


class Contact(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    other_links: list[str] = Field(default_factory=list)


class CVModel(BaseModel):
    name: str
    title: Optional[str] = None
    contact: Contact
    education: List[Education] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    certifications: List[Certification] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list)
    skills_from_work_experience: List[str] = Field(default_factory=list)
