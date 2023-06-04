from Customer import Customer
from Restaurant import Restaurant
from Review import Review
from base import Base, engine

Base.metadata.create_all


#usecase example

# Create customers
customer1 = Customer("Tammy", "Beckham")
customer2 = Customer("Jane", "Kipkemboi")
session.add_all([customer1, customer2])
session.commit()

# Create restaurants
restaurant1 = Restaurant("La Hotela")
restaurant2 = Restaurant("De Hotel")
session.add_all([restaurant1, restaurant2])
session.commit()

# Add reviews
customer1.add_review(restaurant1, 6)
customer1.add_review(restaurant2, 3)
customer2.add_review(restaurant1, 5)

# Access methods
print(customer1.restaurants()) 
print(restaurant1.customers()) 
