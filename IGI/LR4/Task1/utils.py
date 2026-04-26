"""
Purpose: Input validation and UI helper functions.
LW 4 (Task 1)
Version: 1.0
"""

def get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    Validates integer input within a specific range.
    
    Args:
        prompt: Text message displayed to the user before input
        min_val: Minimum allowed value (optional, None means no lower bound)
        max_val: Maximum allowed value (optional, None means no upper bound)
    
    Returns:
        int: Validated integer that satisfies the range constraints
    """
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Error: Enter a value between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_non_empty_string(prompt: str) -> str:
    """Ensures the string input is not empty."""
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Error: This field cannot be empty.")