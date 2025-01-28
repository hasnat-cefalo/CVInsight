from pydantic import BaseModel
from typing import List, Optional

class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    start_date: str
    end_date: str

class Experience(BaseModel):
    company: str
    position: str
    start_date: str
    end_date: str
    description: Optional[str]

class CVModel(BaseModel):
    name: str
    email: str
    phone: str
    education: List[Education]
    experience: List[Experience]
    skills: List[str]
