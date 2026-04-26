"""
Purpose: Geometric figure classes with color management and drawing mixin.
LW 4 (Task 4)
Version 1.0
"""

from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class FigureColor:
    """Manages the color property of a geometric figure."""

    def __init__(self, color_name: str):
        """Initializes with a color name.

        Args:
            color_name (str): The name of the color.
        """
        self._color = color_name

    @property
    def color(self) -> str:
        """Gets the current color."""
        return self._color

    @color.setter
    def color(self, value: str):
        """Sets a new color.

        Args:
            value (str): The color name to set.
        """
        self._color = value

class DrawingMixin:
    """Mixin to provide drawing and saving capabilities."""

    def draw_and_save(self, vertices: list, color: str, info: str, label: str, filename: str):
        """Draws the figure, adds text, and saves to file.

        Args:
            vertices (list): List of (x, y) coordinates.
            color (str): Fill color.
            info (str): Text for the legend/title.
            label (str): Text to sign the figure.
            filename (str): Output filename.
        """
        fig, ax = plt.subplots()    # окно и оси
        poly_patch = Polygon(vertices, closed=True, facecolor=color, edgecolor='black', label='Shape Info')
        ax.add_patch(poly_patch)
        
        all_x, all_y = zip(*vertices)
        limit = max(max(map(abs, all_x)), max(map(abs, all_y))) * 1.5   # добавляем отсуп воркуг фигкры 50%
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')  # одинаковый масштаб по x и y
        
        plt.text(0, 0, label, ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
        plt.title(info)                                               # рамка вокргу текста
        plt.grid(True, linestyle=':')
        
        plt.savefig(filename)
        print(f"[LOG]: Figure saved as '{filename}'.")
        plt.show()

class GeometricFigure(ABC):
    """Abstract base class for all shapes."""

    def __init__(self, name: str):
        """Initializes figure with a name field.

        Args:
            name (str): Name of the geometric figure.
        """
        self._figure_name = name

    def get_figure_name(self) -> str:
        """Returns the name of the figure.

        Returns:
            str: The name of the figure.
        """
        return self._figure_name

    @abstractmethod
    def calculate_area(self) -> float:
        """Abstract method to calculate area."""
        pass

class RegularPolygon(GeometricFigure, DrawingMixin):
    """Represents a regular polygon with n sides."""

    def __init__(self, n: int, a: float, color_name: str):
        """Initializes the polygon and its color object.

        Args:
            n (int): Number of sides.
            a (float): Side length.
            color_name (str): Initial color.
        """
        super().__init__("Regular Polygon")
        self.n = n
        self.a = a
        self.color_obj = FigureColor(color_name)

    def calculate_area(self) -> float:
        """Calculates area using the formula for regular polygons.

        Returns:
            float: Calculated area.
        """
        return (self.n * (self.a ** 2)) / (4 * math.tan(math.pi / self.n))

    def get_info(self) -> str:
        """Returns parameters, color, and area using .format().

        Returns:
            str: Formatted information string.
        """
        return "{0} (Color: {1}): Sides={2}, Length={3}, Area={4:.2f}".format(
            self.get_figure_name(),
            self.color_obj.color,
            self.n,
            self.a,
            self.calculate_area()
        )

    def get_vertices(self) -> list:
        """Computes vertex coordinates for drawing.

        Returns:
            list: List of (x_i, y_i) vertex points.
        """
        radius = self.a / (2 * math.sin(math.pi / self.n))   # радиус описанной окружности
        return [(radius * math.cos(2 * math.pi * i / self.n),
                 radius * math.sin(2 * math.pi * i / self.n)) for i in range(self.n)]