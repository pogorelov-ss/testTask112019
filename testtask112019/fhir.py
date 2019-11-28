from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///:sqlite.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# TODO: custom class with Columns: id, type_code, type_code_system?

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    source_id = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    race_code = Column(String)
    race_code_system = Column(String)
    ethnicity_code = Column(String)
    ethnicity_code_system = Column(String)
    country = Column(String)


class Encouter(Base):
    __tablename__ = 'encouters'

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    type_code = Column(String)
    type_code_system = Column(String)

Patient.encouters = relationship('Encouter', order_by=Encouter.id, back_populates="patient")


class Procedure(Base):
    __tablename__ = 'procedures'

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    encouter_id = Column(Integer, ForeignKey('encouters.id'))
    procedure_date = Column(Date)
    type_code = Column(String)
    type_code_system = Column(String)

Patient.procedures = relationship('Procedure', order_by=Procedure.id, back_populates="patient")
Encouter.procedures = relationship('Procedure', order_by=Procedure.id, back_populates="encouter")


class Observation(Base):
    __tablename__ = 'observations'

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    encouter_id = Column(Integer, ForeignKey('encouters.id'))
    observation_date = Column(Date)
    type_code = Column(String)
    type_code_system = Column(String)
    value = Column(Numeric) # TODO: extra params?
    unit_code = Column(String)


Patient.observations = relationship('Observation', order_by=Observation.id, back_populates="patient")
Encouter.observations = relationship('Observation', order_by=Observation.id, back_populates="encouter")