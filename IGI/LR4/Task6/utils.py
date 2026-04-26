"""
Purpose: Function for loading data from file.
LW 4 (Task 6)
Version 1.0
"""

import pandas as pd
import os

def load_csv_data(file_path: str) -> pd.DataFrame:
    """Loads a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data or an empty DataFrame if failed.
    """
    if not os.path.exists(file_path):
        print(f"[ERROR]: File {file_path} not found.")
        return pd.DataFrame()
    
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"[ERROR]: Loading failed: {e}")
        return pd.DataFrame()