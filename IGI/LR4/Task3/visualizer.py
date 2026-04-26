"""
Purpose: Mixin for plotting function results using Matplotlib.
LW 4 (Task 3)
Version 1.0
"""

import matplotlib.pyplot as plt

class VisualizerMixin:
    """Provides methods for data visualization."""

    def plot_data(self, x_vals: list, series_vals: list, math_vals: list, filename: str = "result_plot.png"):
        """Creates and saves a comparison plot.

        Args:
            x_vals (list): X-axis coordinates.
            series_vals (list): Y-axis values from the power series.
            math_vals (list): Y-axis values from the math module.
            filename (str): The filename to save the resulting plot.
        """
        plt.figure(figsize=(10, 6))
        
        plt.plot(x_vals, series_vals, color='crimson', label='Series F(x)', marker='o', linestyle='-', alpha=0.8)
        plt.plot(x_vals, math_vals, color='navy', label='Math Module F(x)', linestyle='--', linewidth=2)
        
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        plt.grid(True, linestyle=':', alpha=0.6)
        
        plt.title("Comparison: Power Series vs Math.log(1-x)")
        plt.xlabel("Argument (x)")
        plt.ylabel("Function Value (F(x))")
        plt.legend()

        if x_vals:
            mid_idx = len(x_vals) // 2
            plt.annotate('Median Point', xy=(x_vals[mid_idx], series_vals[mid_idx]), 
                         xytext=(x_vals[mid_idx] - 0.2, series_vals[mid_idx] + 0.5),
                         arrowprops=dict(facecolor='green', shrink=0.05),
                         fontsize=10)                       # отступ стрелки
            plt.text(x_vals[0], series_vals[0], "Start point", color='red', fontsize=9)

        plt.savefig(filename)
        print(f"[LOG]: Visualization successfully saved to '{filename}'.")
        plt.show()