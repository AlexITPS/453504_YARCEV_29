"""
Purpose: Data models with advanced properties and mixins.
LW 4 (Task 1)
Version: 1.0
"""

from abc import ABC, abstractmethod

class LoggerMixin:
    """Mixin to provide logging capabilities."""
    def log_action(self, action: str):
        """Logs the action performed on the object."""
        print(f"[LOG]: {self.__class__.__name__} was {action}")

class Person(ABC):
    """Abstract base class for all human-related entities."""
    def __init__(self, full_name: str):
        self._full_name = full_name  

    @property
    def full_name(self):
        """Property: Getter for the full name."""
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        """Property: Setter for the full name with basic validation."""
        if len(value) < 2:
            raise ValueError("Name too short")
        self._full_name = value

    @abstractmethod
    def get_info(self):
        """Abstract method to be implemented by subclasses."""
        pass

class Student(Person, LoggerMixin):
    """
    Class representing a student.
    Demonstrates: static attribute, super(), mixins, properties.
    """
    total_students = 0 

    def __init__(self, full_name: str, day: int, month: int, year: int):
        super().__init__(full_name)
        self.day = day
        self._month = month  
        self.year = year    
        Student.total_students += 1
        self.log_action("initialized")

    @property
    def month(self):
        """Getter for birthday month of student."""
        return self._month

    @month.setter
    def month(self, value):
        """Setter for month with specific range check."""
        if 1 <= value <= 12:
            self._month = value
        else:
            raise ValueError("Month must be in range 1-12")

    def __str__(self):
        """Polymorphism: Human-readable string. """
        return f"{self._full_name.ljust(20)} | Birthday: {self.day:02d}.{self._month:02d}.{self.year}"

    def get_info(self):
        """Implementation of abstract method."""
        return f"Student record for {self._full_name}"

    def to_dict(self):
        """Converts object data to dictionary for serialization."""
        return {
            "full_name": self._full_name,
            "day": self.day,
            "month": self._month,
            "year": self.year
        }