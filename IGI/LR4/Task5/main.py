"""
Purpose: Main module for NumPy investigation and matrix tasks.
LW 4 (Task 5)
Version: 1.0
Author: Yarcev A.A.
Date: 21.04.2026
"""

import numpy as np
import matrix_models
import utils

def demonstrate_numpy_features():
    """Func demonstrates various NumPy array creation functions."""
    print("\n--- NumPy Operations Demonstration ---")
    
    arr = np.array([1, 2, 3])
    print(f"Array from list: {arr}")
    
    # 2 x 2
    print(f"Zeros:\n{np.zeros((2, 2))}") 
    print(f"Ones:\n {np.ones((2, 2))}")
    
    demo_mat = np.random.randint(10, 30, (3, 3))
    print(f"Before Slicing:\n{demo_mat}")
    print(f"Slicing (first 2 rows, last 2 columns):\n{demo_mat[:2, 1:]}")
                # срез до второй строки не включительно (индексация с 0) и с 1 столбца включая до конца
def run_task():
    """Executes the main assignment tasks."""
    print("\n=== NumPy Matrix Analysis Task ===")
    
    rows = utils.get_int_input("Enter number of rows (n): ")
    cols = utils.get_int_input("Enter number of columns (m): ")
    
    matrix = utils.generate_random_matrix(rows, cols)
    print(f"\nGenerated Matrix:\n{matrix}")
    
    processor = matrix_models.NumPyProcessor(matrix)
    results = processor.process_analysis()
    
    print(f"\n--- Analysis Results ---")
    print(f"1. Sum of elements below main diagonal: {results['Sum below diagonal']}")
    print(f"2. Main diagonal elements: {results['Diagonal elements']}")
    print(f"3. Std Deviation for main diagonal (NumPy function): {results['Std Dev (NumPy)']}")
    print(f"4. Std Deviation for main diagonal (Manual formula): {results['Std Dev (Manual)']}")
    
    print("\n--- Statistical Overview ---")
    print(f"Mean: {results['Matrix Mean']:.2f}")
    print(f"Median: {results['Matrix Median']:.2f}")
    print(f"Variance: {results['Matrix Variance']:.2f}")
    
    if rows > 1:
        corr = np.corrcoef(matrix)
        print("\nCorrelation Coefficient Matrix (between rows):")
        print(np.round(corr, 2))

def main():
    """Main program loop."""
    demonstrate_numpy_features()
    
    while True:
        run_task()
        
        repeat = input("\nRun analysis again? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Exiting. Goodbye!")
            break

if __name__ == "__main__":
    main()