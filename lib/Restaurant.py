from sqlalchemy import Column, Integer, String
from base import Base, engine, session

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_keys=True)
    name = Column(String)

    def __init__ (self, name):
        self.name = name

    def name(self):
        return self.name

    def reviews(self):
        return [review for review in self.reviews]
    
    def customers(self):
        return [review.customer for review in self.reviews]
    
    def average_star_rating(self):
        review_ratings = [review.rating for review in self.reviews]
        if review_ratings:
            return sum(review_ratings) / len(review_ratings)
        else:
            return 0
        
    @classmethod
    def all(cls):
        return session.query(cls).all()