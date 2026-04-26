"""
Purpose: Entry point for Diabetes Dataset analysis (Pandas Lab).
LW 4 (Task 6)
Version: 1.0
Author: Yarcev A.A.
Date: 21.04.2026
"""

import pandas as pd
import diabetes_models
import utils

def show_pandas_features(df: pd.DataFrame):
    """Demonstrates Pandas operations.

    Args:
        df (pd.DataFrame): The main dataframe.
    """
    print("\n--- PANDAS CAPABILITIES ---")
    
    # Доступ по позиции (первые 3 строки, первые 3 столбца) -> матрица 3 x 3
    print("1. Slicing rows 0-3 and cols 0-3 using .iloc:")
    print(df.iloc[:3, :3])
    
    # Доступ по метке (вывод: одно значение)
    print("\n2. Accessing a specific cell via .loc (Index 0, Column 'Age'):")
    print(f"Result: {df.loc[0, 'Age']}")
    
    print("\n3. Dataframe statistics and summary:")
    df.info()

def execute_main_analysis():
    """Reads data and coordinates the analysis tasks."""
    data_file = "diabetes.csv"
    df = utils.load_csv_data(data_file)

    if df.empty:
        return

    show_pandas_features(df)

    processor = diabetes_models.DiabetesProcessor(df)
    print(f"\n[SYSTEM]: Object created: {processor}")

    categories, ratio = processor.run_analysis()

    print("\n--- RESULTS: Glucose Categories ---")
    result_display = pd.DataFrame({
        'Original_Glucose': df['Glucose'],
        'Category': categories
    })
    print(result_display.head(10))

    print("\n--- RESULTS: Statistical Ratio ---")
    print(f"The mean BMI for max glucose patients is {ratio} "
          f"times the mean BMI of min glucose patients.")

def main():
    """Main loop for the application."""
    while True:
        execute_main_analysis()
        
        repeat = input("\nRepeat analysis? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Shutting down. Goodbye!")
            break

if __name__ == "__main__":
    main()