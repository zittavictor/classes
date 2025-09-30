"""
Module: walk.py
Developer: Your Name
Date Created: 2025-09-30
Date Last Modified: 2025-09-30
Description: Defines the Walk class for calculating miles walked.
"""

INCHES_PER_MILE = 63360

class Walk:
    def __init__(self, name, steps, step_length):
        self.__name = name
        self.__steps = steps
        self.__step_length = step_length

    # Getters and setters
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_steps(self):
        return self.__steps
    def set_steps(self, steps):
        self.__steps = steps

    def get_step_length(self):
        return self.__step_length
    def set_step_length(self, step_length):
        self.__step_length = step_length

    # Calculate miles walked
    def miles_walked(self):
        return (self.__steps * self.__step_length) / INCHES_PER_MILE
