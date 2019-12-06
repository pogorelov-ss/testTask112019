from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import sessionmaker, relationship
import jsonlines
import os

engine = create_engine('postgresql+psycopg2://admin:example@localhost:5432/fhir', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# TODO: custom class with Columns: id, type_code, type_code_system?
# TODO: add back_populates

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
    source_id = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    type_code = Column(String)
    type_code_system = Column(String)


# Patient.encouters = relationship('Encouter', order_by=Encouter.id, back_populates="patient")


class Procedure(Base):
    __tablename__ = 'procedures'

    id = Column(Integer, primary_key=True)
    source_id = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    encouter_id = Column(Integer, ForeignKey('encouters.id'))
    procedure_date = Column(Date)
    type_code = Column(String)
    type_code_system = Column(String)


# Patient.procedures = relationship('Procedure', order_by=Procedure.id, back_populates="patient")
# Encouter.procedures = relationship('Procedure', order_by=Procedure.id, back_populates="encouter")


class Observation(Base):
    __tablename__ = 'observations'

    id = Column(Integer, primary_key=True)
    source_id = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    encouter_id = Column(Integer, ForeignKey('encouters.id'))
    observation_date = Column(Date)
    type_code = Column(String)
    type_code_system = Column(String)
    value = Column(Numeric)  # TODO: extra params?
    unit_code = Column(String)


# Patient.observations = relationship('Observation', order_by=Observation.id, back_populates="patient")
# Encouter.observations = relationship('Observation', order_by=Observation.id, back_populates="encouter")

def import_data(path):
    if os.path.isdir(path) is False:
        return 'path not found'
    else:
        pass
    result = list()
    result = import_patients(path)
    result.append(import_encouters(path))
    return result


def import_patients(path):
    patients_file_path = f'{path}/Patient.ndjson'
    results = list()
    with jsonlines.open(patients_file_path) as reader:
        for obj in reader.iter(type=dict, skip_invalid=True):
            try:
                extensions = obj.get('extension')
                for extension in extensions:
                    if 'valueCodeableConcept' in extension.keys():
                        if extension['valueCodeableConcept']['text'] == 'race':
                            race_code = extension['valueCodeableConcept']['coding'][0]['code']
                            race_code_system = extension['valueCodeableConcept']['coding'][0]['system']
                        if extension['valueCodeableConcept']['text'] == 'ethnicity':
                            ethnicity_code = extension['valueCodeableConcept']['coding'][0]['code']
                            ethnicity_code_system = extension['valueCodeableConcept']['coding'][0]['system']
                patient = Patient(
                    source_id=obj.get('id'),
                    birth_date=obj.get('birthDate'),
                    gender=obj.get('gender'),
                    country=obj.get('address')[0].get('country'),
                    race_code=race_code,
                    race_code_system=race_code_system,
                    ethnicity_code=ethnicity_code,
                    ethnicity_code_system=ethnicity_code_system
                )
                session.add(patient)

            except Exception as e:
                results.append(f'{e} error for patient {obj["id"]}')
    session.commit()
    return results

def import_encouters(path):
    encouters_file_path = f'{path}/Encounter.ndjson'
    results = list()
    last_patient_id = None
    last_patient_source_id = None
    with jsonlines.open(encouters_file_path) as reader:
        for obj in reader.iter(type=dict, skip_invalid=True):
            try:
                patient_source_id = obj['subject']['reference'].split('/')[1]
                if last_patient_source_id == patient_source_id:
                    patient_id = last_patient_id
                else:
                    patient_id = session.query(Patient.id).filter(Patient.source_id == patient_source_id).first()
                if patient_id is not None:
                    ecouter = Encouter(
                        source_id=obj.get('id'),
                        patient_id=patient_id[0],
                        start_date=obj['period']['start'],
                        end_date=obj['period']['end'],
                        type_code=obj['type'][0]['coding'][0]['code'],
                        type_code_system=obj['type'][0]['coding'][0]['system']
                    )
                    session.add(ecouter)
                    last_patient_source_id = patient_source_id
                    last_patient_id = patient_id
            except Exception as e:
                results.append(f'{e} error for patient {obj["id"]}')
    session.commit()
    return results
