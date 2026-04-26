"""
Purpose: Math logic for power series expansion of ln(1-x).
LW 4 (Task 3)
Version 1.0
"""

import math
from abc import ABC, abstractmethod

class SeriesCalculator(ABC):
    """Abstract base class for series calculators."""

    def __init__(self, eps: float):
        """Initializes the calculator with a specific precision.

        Args:
            eps (float): The target precision for the series calculation.
        """
        self._eps = eps

    @property
    def eps(self) -> float:
        """float: The precision used for calculations."""
        return self._eps

    @eps.setter
    def eps(self, value: float):
        """Sets the precision value with validation.

        Args:
            value (float): Precision value.
        """
        if value <= 0:
            raise ValueError("Precision must be a positive value.")
        self._eps = value

    @abstractmethod
    def calculate(self, x: float):
        """Calculates the function value at point x.

        Args:
            x (float): The argument value.
        """
        pass

class LnCalculator(SeriesCalculator):
    """Calculates ln(1-x) using the power series: -x - x^2/2 - x^3/3..."""
    
    def __init__(self, eps: float, max_iter: int = 500):
        """Initializes the Ln calculator.

        Args:
            eps (float): Target precision.
            max_iter (int): Maximum number of iterations.
        """
        super().__init__(eps)
        self.max_iter = max_iter

    def calculate(self, x: float) -> tuple:
        """Computes the sum of the power series for ln(1-x).

        Args:
            x (float): Argument value where |x| < 1.

        Returns:
            tuple: (series_sum, iterations, math_value)

        Raises:
            ValueError: If x is not within the convergence range (-1, 1).
        """
        if not (-1 < x < 1):
            raise ValueError(f"Argument x={x} is out of convergence range (-1, 1).")
        
        sum_value = 0.0
        n = 1
        while n <= self.max_iter:
            term = -(x**n / n)
            sum_value += term
            if abs(term) < self._eps:
                break
            n += 1
        
        return sum_value, n, math.log(1 - x)

    def __str__(self) -> str:
        """Returns a string representation of the calculator."""
        return f"LnCalculator(eps={self._eps}, max_iter={self.max_iter})"