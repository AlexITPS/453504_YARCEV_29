"""
Purpose: Statistical and classification logic for Pandas data.
LW 4 (Task 6)
Version 1.0
"""

import pandas as pd

class ClassificationMixin:
    """Provides categorization methods for medical data."""

    def categorize_glucose(self, series: pd.Series) -> pd.Series:
        """Classifies glucose levels into categories.

        Args:
            series (pd.Series): The glucose values.

        Returns:
            pd.Series: Categories: 'normal' (<140) or 'high' (>=140).
        """
        return series.apply(lambda x: "normal" if x < 140 else "high")

class StatisticsMixin:
    """Provides methods for complex data indexing and comparison."""

    def get_bmi_comparison_ratio(self, dataframe: pd.DataFrame) -> float:
        """Calculates BMI ratio between max and min glucose groups.

        Args:
            dataframe (pd.DataFrame): The diabetes dataset.

        Returns:
            float: Ratio of mean BMIs rounded to two decimal places.
        """
        max_val = dataframe['Glucose'].max()
        min_val = dataframe['Glucose'].min()

        # выбираем столбец BMI только для строк с минимальным и максимальным уровнем глюкозы
        mean_bmi_max = dataframe.loc[dataframe['Glucose'] == max_val, 'BMI'].mean()
        mean_bmi_min = dataframe.loc[dataframe['Glucose'] == min_val, 'BMI'].mean()
        
        if mean_bmi_min == 0 or pd.isna(mean_bmi_min):
            return 0.0

        return round(mean_bmi_max / mean_bmi_min, 2)