from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from database import engine  # database.py에서 engine을 가져옵니다.

Base = declarative_base()

class Patent(Base):
    __tablename__ = "patents"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    application_number = Column(Integer, index=True)
    application_date = Column(Date)
    publication_number = Column(Integer, index=True)
    publication_date = Column(Date)
    announcement_number = Column(Integer, index=True)
    announcement_date = Column(Date)
    registration_number = Column(Integer, index=True)
    registration_date = Column(Date)
    title = Column(Text)
    ipc_classification = Column(Text) 
    classification = Column(String(1))
    applicant = Column(Text)
    inventor = Column(Text)
    agent = Column(Text)
    international_application_number = Column(String, index=True)
    international_application_date = Column(Date)
    international_publication_number = Column(String, index=True)
    international_publication_date = Column(Date)
    abstract = Column(Text)
    cpc_classification = Column(Text)
    priority_information = Column(Text)
    designated_states = Column(Text)
    docdb_family_id = Column(String, index=True)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)
