from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:sqlite.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    # __tablename__ = self.__name__.lower()
    id = Column(Integer, primary_key=True)
    source_id = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    race_code = Column(String)
    race_code_system = Column(String)
    ethnicity_code = Column(String)
    ethnicity_code_system = Column(String)
    country = Column(String)
