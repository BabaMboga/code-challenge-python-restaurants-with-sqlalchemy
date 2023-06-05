from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base, engine, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#configuring the database connection
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    rating = Column(Integer)

    customer = relationship('Customer', backref='reviews')
    restaurant = relationship('Restaurant', backref='reviews')

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def rating(self):
        return self.rating
    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return session.query(cls).all()