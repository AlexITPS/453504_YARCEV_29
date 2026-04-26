"""
Purpose: File operations with specific exception handling.
LW 4 (Task 1)
Version: 1.0
"""

import csv
import pickle
import os

def save_to_csv(filename: str, data: list):
    """Saves data to CSV. Handles PermissionError."""
    try:
        if not data: return
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    except PermissionError:
        print(f"Error: No permission to write to {filename}")
    except Exception as e:
        print(f"An unexpected error occurred during write CSV save: {e}")

def load_from_csv(filename: str):
    """Loads from CSV. Handles FileNotFoundError."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Warning: File {filename} not found.")
        return []

def save_to_pickle(filename: str, data: list):
    """Saves data to Pickle."""
    try:
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    except pickle.PickleError as e:
        print(f"Pickling error: {e}")

def load_from_pickle(filename: str):
    """Loads data from Pickle with additional checks."""
    try:
        if not os.path.exists(filename):
            return []
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except (pickle.UnpicklingError, EOFError):
        print(f"Error: Pickle file {filename} is corrupted or empty.")
        return []
    except PermissionError:
        print(f"Error: Access denied to {filename}.")
        return []