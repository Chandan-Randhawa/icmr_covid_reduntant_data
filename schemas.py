from sqlalchemy import (Column, BigInteger, String, Float,
                        DateTime, Integer, SmallInteger, Boolean, Text,ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from db import Base
from db import engine

class IcmrCovidDetails(Base):
    __tablename__ = 'icmrcoviddetails'
    user_id = Column(Integer , primary_key=True)
    icmr_id = Column(String(1024))
    clinical_id = Column(String(1024),unique = True)
    age = Column(String(1024))
    age_in = Column(String(1024))
    gender = Column(String(1024))
    patient_category = Column(String(1024))
    state_residence = Column(String(1024))
    district_residence = Column(String(1024))
    lab_id = Column(String(1024))
    date_sample_collection = Column(String(1024))
    date_sample_received = Column(String(1024))
    date_of_sample_tested = Column(String(1024))
    symptoms = Column(String(2048))
    underlying_medical_condition = Column(String(2048))
    testing_kit_used = Column(String(2048))
    egene_screening = Column(String(1024))
    ct_value_screening = Column(String(1024))
    rdrp_confirmatory = Column(String(1024))
    ct_value_rdrp = Column(String(1024))
    orf1b_confirmatory = Column(String(1024))
    ct_value_orf1b = Column(String(1024))
    final_test_result = Column(String(256))
    entry_date = Column(String(1024))
    updated_on = Column(String(1024))

Base.metadata.create_all(engine)
