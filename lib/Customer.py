from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base, engine, session
from Review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#configuring the database connection
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    def add_review(self, restaurant, rating):
        review = Review(customer=self, restaurant=restaurant, rating=rating)
        session.add(review)
        session.commit()

    def restaurants(self):
        return [review.restaurant for review in self.reviews]
    
    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod
    def all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(given_name=name).first()
    
    @classmethod
    def find_all_by_given_name(cls, name):
        return session.query(cls).filter_by(given_name=name).all()