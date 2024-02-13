from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class PatentBase(BaseModel):
    country: str
    application_number: int
    application_date: date
    publication_number: int
    publication_date: date
    announcement_number: int
    announcement_date: date
    registration_number: int
    registration_date: date
    title: str
    ipc_classification: List[str] = []
    classification: str
    applicant: str
    inventor: str
    agent: str
    international_application_number: Optional[str] = None
    international_application_date: Optional[date] = None
    international_publication_number: Optional[str] = None
    international_publication_date: Optional[date] = None
    abstract: str
    cpc_classification: List[str] = []
    priority_information: Optional[str] = None
    designated_states: Optional[str] = None
    docdb_family_id: Optional[str] = None

# 특허 생성을 위한 스키마
class PatentCreate(PatentBase):
    pass

# 특허 조회를 위한 스키마
class PatentRead(PatentBase):
    id: int

    class Config:
        orm_mode = True

# 특허 업데이트를 위한 스키마
class PatentUpdate(PatentBase):
    pass

# 전체 특허 정보에 대한 스키마, API 응답용
class Patent(PatentBase):
    id: int

    class Config:
        orm_mode = True
