"""
Purpose: Input validation for shape parameters.
LW 4 (Task 4)
Version 1.0
"""

def get_valid_num(prompt: str, min_val: float, is_int: bool = False):
    """Validator for numeric input.

    Args:
        prompt (str): Text for input.
        min_val (float): Minimum allowed value.
        is_int (bool): If True, forces integer conversion.

    Returns:
        Number: Validated input.
    """
    while True:
        try:
            val = float(input(prompt))
            if val < min_val:
                print(f"Error: Value must be at least {min_val}.")
                continue
            return int(val) if is_int else val
        except ValueError:
            print("Error: Invalid numerical format.")