"""
Purpose: Mixin for statistical analysis of calculated sequences.
LW 4 (Task 3)
Version 1.0
"""

import statistics

class StatisticsMixin:
    """Provides statistical analysis methods for numerical sequences."""

    def get_full_statistics(self, data: list) -> dict:
        """Calculates mean (среднее арифмитическое), median, mode, variance (дисперсия), and standard deviation.

        Args:
            data (list): A list of numerical results.

        Returns:
            dict: Statistical parameters or an error message if data is insufficient.
        """
        if not data or len(data) < 2:
            return {"Error": "Incorrect data for statistical analysis (min 2 points)."}

        try:
            mode_val = statistics.mode(data)    # мода - значение, которое встречается чаще всего
        except statistics.StatisticsError:
            mode_val = "Multiple/None"

        return {
            "Arithmetic Mean": statistics.mean(data),  # mean
            "Median": statistics.median(data),
            # Средний элемент в упорядоченном!!! ряду чисел (то есть сортировка необходима).
            # Если n - нечетное, то Me = x_((n+1)/2)
            # Если n - четное, то Me = ( x_((n)/2) + x_((n/2) + 1) ) / 2
            "Mode": mode_val,
            "Variance": statistics.variance(data),
            # Мера разброса данных относительно среднего (), считаем по формуле:
            # s^2 = (sum(i=1 .. n) (x_i - mean)^2 ) / n - 1
            "Std Deviation (СКО)": statistics.stdev(data)
            #std = sqrt(s^2)
        }   