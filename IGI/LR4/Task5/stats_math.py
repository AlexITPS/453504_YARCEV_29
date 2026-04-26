"""
Purpose: Mixin for manual mathematical formulas without library helpers.
LW 4 (Task 5)
Version 1.0
"""

import math
import numpy as np

class ManualStatsMixin:
    """Provides manual implementations of statistical formulas."""

    def calculate_std_manual(self, data: np.ndarray) -> float:
        """Calculates standard deviation using the mathematical formula.

        Formula: sqrt(sum((x_i - mean)^2) / N)

        Args:
            data (np.ndarray): 1D array of numbers.

        Returns:
            float: Calculated standard deviation.
        """
        if len(data) == 0:
            return 0.0
            
        n = len(data)
        mean_val = sum(data) / n
        
        variance_sum = sum((x - mean_val) ** 2 for x in data)
        return math.sqrt(variance_sum / n)