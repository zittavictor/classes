"""
Module: car_rental.py
Developer: Your Name
Date Created: 2025-09-30
Date Last Modified: 2025-09-30
Description: Defines the Car_Rental class for calculating rental charges.
"""

DAILY_RATE = 62.50
MILE_RATE = 0.57

class Car_Rental:
    def __init__(self, customer, start_odometer, end_odometer, days):
        self.customer = customer
        self.start_odometer = start_odometer
        self.end_odometer = end_odometer
        self.days = days
        self.__rental_charge = self.__calculate_charge()

    def __calculate_charge(self):
        miles = self.end_odometer - self.start_odometer
        return (DAILY_RATE * self.days) + (MILE_RATE * miles)

    @property
    def rental_charge(self):
        return self.__calculate_charge()

    def __str__(self):
        miles = self.end_odometer - self.start_odometer
        return (f"Customer Name: {self.customer}\n"
                f"Number of Rental Days: {self.days}\n"
                f"Miles Driven: {miles}\n"
                f"Rental Charge: ${self.rental_charge:.2f}")
