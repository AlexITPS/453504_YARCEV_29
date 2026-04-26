"""
Purpose: OOP models for analyzing the Diabetes dataset.
LW 4 (Task 6)
Version 1.0
"""

import pandas as pd
from abc import ABC, abstractmethod
from analysis_mixins import ClassificationMixin, StatisticsMixin

class BaseAnalyzer(ABC):
    """Abstract base class for data analysis."""

    def __init__(self, df: pd.DataFrame):
        """Initializes the analyzer with a DataFrame.

        Args:
            df (pd.DataFrame): The dataset to process.
        """
        self._df = df

    @property
    def dataframe(self) -> pd.DataFrame:
        """pd.DataFrame: Getter for the protected dataframe."""
        return self._df

    @abstractmethod
    def run_analysis(self):
        """Abstract method for processing data logic."""
        pass

class DiabetesProcessor(BaseAnalyzer, ClassificationMixin, StatisticsMixin):
    """Main processor for diabetes data using inheritance and mixins."""

    def __init__(self, df: pd.DataFrame):
        """Initializes the processor using the super() constructor.

        Args:
            df (pd.DataFrame): Input diabetes data.
        """
        super().__init__(df)

    def run_analysis(self) -> tuple:
        """Performs classification and ratio calculation tasks.

        Returns:
            tuple: (Categorized Series, BMI comparison ratio)
        """
        # Часть А
        categories = self.categorize_glucose(self._df['Glucose'])
        
        # Часть Б
        bmi_ratio = self.get_bmi_comparison_ratio(self._df)
        
        return categories, bmi_ratio

    def __str__(self) -> str:
        """Returns basic information about the processor."""
        return f"DiabetesProcessor analyzing {len(self._df)} patient records."