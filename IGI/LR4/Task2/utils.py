"""
Purpose: Input validation and UI helper functions.
LW 4 (Task 2)
Version: 1.0
"""

def get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Safely gets an integer within a range."""
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
    """Ensures input is not just whitespace."""
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Error: Field cannot be empty.")