"""
Purpose: Main application module for ln(1-x) series analysis.
LW 4 (Task 3) - Extension for Task 1 from LW 3
Version: 1.0
Author: Yarcev A.A.
Date: 19.04.2026
"""

import math_logic
import stats_processor
import visualizer
import sequence_init
import utils

class AnalysisApp(stats_processor.StatisticsMixin, visualizer.VisualizerMixin):
    """Calculation, statistical analysis, and visualization."""

    def __init__(self, eps: float):
        """Initializes the application.

        Args:
            eps (float): Precision for the power series.
        """
        self.calc = math_logic.LnCalculator(eps)

    def run(self, x_list: list):
        """Processes a list of x values and displays results.

        Args:
            x_list (list): Values of x to be analyzed.
        """
        table_results = []
        y_series = []
        y_math = []
        valid_x = []

        for x in x_list:
            try:
                f_x, n, m_x = self.calc.calculate(x)
                table_results.append((x, n, f_x, m_x, self.calc.eps))
                y_series.append(f_x)
                y_math.append(m_x)
                valid_x.append(x)
            except ValueError as e:
                print(f"[ERROR]: {e}")

        utils.display_results(table_results)

        stats = self.get_full_statistics(y_series)
        print("\n--- STATISTICAL ANALYSIS ---")
        if "Error" in stats:
            print(stats["Error"])
        else:
            for key, val in stats.items():
                if isinstance(val, float):
                    print(f"{key:.<20} {val:>12.6f}")
                else:
                    print(f"{key:.<20} {val:>12}")

        if valid_x:
            self.plot_data(valid_x, y_series, y_math)

@utils.repeat_decorator
def start_app():
    """Starts the application with user-defined parameters."""
    print("\n" + "="*50)
    print("Task 3: Power Series ln(1-x) Analysis")
    print("="*50)

    precision = utils.safe_float_input("Enter target precision (eps): ")
    
    start = utils.safe_float_input("Start x (-1 < x < 1): ")
    end = utils.safe_float_input("End x (-1 < x < 1): ")
    count = utils.safe_int_input("Number of points: ")
    
    x_sequence = sequence_init.init_from_generator(start, end, count)
    
    app = AnalysisApp(precision)
    app.run(x_sequence)

if __name__ == "__main__":
    start_app()