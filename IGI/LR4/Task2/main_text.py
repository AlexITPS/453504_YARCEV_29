"""
Purpose: Main testing module for Text Analysis.
LW 4 (Task 2) - Regex Text Analysis
Version: 1.0
Author: Yarcev A.A.
Date: 18.04.2026
"""

import text_processor
import regex_ops
import utils
import os
import zipfile

def show_zip_info(zip_name):
    """Requirement: Get info about file in archive."""
    if not os.path.exists(zip_name): return
    try:
        with zipfile.ZipFile(zip_name, 'r') as z:
            print("\n--- METADATA ---")
            for info in z.infolist():
                print(f"File inside: {info.filename}")
                print(f"Original size: {info.file_size} bytes")
                print(f"Compressed size: {info.compress_size} bytes")
    except zipfile.BadZipFile:
        print("Archive error.")

def process_analysis():
    """Logic for task execution."""
    filename = "input.txt"
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Hello! Is this v3nding machine? Yes;---))) s-word should go. 127.0.0.1")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        analyzer = text_processor.AdvancedTextAnalyzer(content)
        print(f"\n[SYSTEM]: Starting {analyzer}")
        
        results = analyzer.run_full_analysis()

        report_lines = [f"{k}: {v}" for k, v in results.items()]
        full_report = "\n".join(report_lines)
        print("\n--- ANALYSIS RESULTS ---\n" + full_report)

        out_file = "output.txt"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("TEXT ANALYSIS REPORT\n" + "="*20 + "\n" + full_report)

        analyzer.archive_results(out_file, "results.zip")
        show_zip_info("results.zip")

    except IOError as e:
        print(f"File error: {e}")

def main():
    while True:
        print("\n=== TEXT ANALYSIS MENU (LW 2) ===")
        print("1. Run analysis on 'input.txt'")
        print("2. Test IP Validator (with regex_strip)")
        print("3. Exit")
        
        choice = utils.get_int_input("Action: ", 1, 3)

        if choice == 1:
            process_analysis()
        elif choice == 2:
            raw_ip = input("Enter IP (spaces will be stripped): ")
            if regex_ops.is_valid_ip(raw_ip):
                print(f"Result: '{raw_ip.strip()}' is a VALID IP.")
            else:
                print(f"Result: '{raw_ip.strip()}' is INVALID.")
        elif choice == 3:
            print("Program finished.")
            break

if __name__ == "__main__":
    main()