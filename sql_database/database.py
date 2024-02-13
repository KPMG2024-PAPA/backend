from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import get_mysql_setting
from dotenv import load_dotenv
import os

load_dotenv()  # 환경 변수 로드

settings = get_mysql_setting()

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    settings.MYSQL_USER,
    settings.MYSQL_PASSWORD,
    settings.MYSQL_HOST,
    settings.MYSQL_PORT,
    settings.MYSQL_DATABASE,
)

class engineconn:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=500)  # 오타 수정

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn

db_engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=db_engine)
