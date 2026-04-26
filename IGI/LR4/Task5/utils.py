"""
Purpose: Matrix generation and input validation.
LW 4 (Task 5)
Version 1.0
"""

import numpy as np

def get_int_input(prompt: str, min_val: int = 1) -> int:
    """Safely gets integer input from user.

    Args:
        prompt (str): Text message.
        min_val (int): Minimum allowed value.

    Returns:
        int: Validated integer.
    """
    while True:
        try:
            val = int(input(prompt))
            if val >= min_val:
                return val
            print(f"Error: Value must be at least {min_val}.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def generate_random_matrix(n: int, m: int) -> np.ndarray:
    """Generates a random integer matrix using NumPy.

    Args:
        n (int): Rows.
        m (int): Columns.

    Returns:
        np.ndarray: Randomized matrix.
    """
    return np.random.randint(0, 100, size=(n, m))  # generate value from 0 to 99