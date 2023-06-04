from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base, engine, session

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)