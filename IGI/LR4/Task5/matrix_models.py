"""
Purpose: NumPy matrix analysis models.
LW 4 (Task 5)
Version 1.0
"""

from abc import ABC, abstractmethod
import numpy as np
import stats_math

class BaseMatrixAnalyzer(ABC):
    """Abstract base class for matrix analysis."""

    def __init__(self, matrix: np.ndarray):
        """Initializes with a NumPy matrix.

        Args:
            matrix (np.ndarray): The matrix to analyze.
        """
        self._matrix = matrix

    @property
    def matrix(self) -> np.ndarray:
        """np.ndarray: Getter for the underlying matrix."""
        return self._matrix

    @abstractmethod
    def process_analysis(self):
        """Abstract method for full analysis."""
        pass

class NumPyProcessor(BaseMatrixAnalyzer, stats_math.ManualStatsMixin):
    """Processor that doing specific NumPy tasks and formulas."""

    def __init__(self, matrix: np.ndarray):
        """Initializes the processor.

        Args:
            matrix (np.ndarray): Integer matrix.
        """
        super().__init__(matrix)

    def get_sum_below_diagonal(self) -> int:
        """Calculates the sum of elements below the main diagonal.

        Returns:
            int: Sum of elements.
        """
        # нижняя треугольная матрица, не включая главную диагональ (k=-1)
        return np.tril(self._matrix, k=-1).sum()    

    def get_diagonal_elements(self) -> np.ndarray:
        """Extracts elements of the main diagonal.

        Returns:
            np.ndarray: 1D array of diagonal elements.
        """
        return np.diag(self._matrix)

    def process_analysis(self) -> dict:
        """Executes the analysis tasks required by the problem.

        Returns:
            dict: Results of calculations and library demonstrations.
        """
        diag_elements = self.get_diagonal_elements()
        
        return {
            "Sum below diagonal": self.get_sum_below_diagonal(),
            "Diagonal elements": diag_elements,
            "Std Dev (NumPy)": round(np.std(diag_elements), 2), # deviation (стандартное отклонение)
            "Std Dev (Manual)": round(self.calculate_std_manual(diag_elements), 2),
            "Matrix Mean": np.mean(self._matrix),
            "Matrix Median": np.median(self._matrix),
            "Matrix Variance": np.var(self._matrix)     # дисперсия
        }

    def __str__(self) -> str:
        """Returns string info about the matrix dimensions."""      
        return f"NumPyProcessor: {self._matrix.shape[0]}x{self._matrix.shape[1]} matrix"
            # matrix.shape return (number rows, number of columns)