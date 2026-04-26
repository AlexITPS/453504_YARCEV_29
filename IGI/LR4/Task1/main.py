"""
Purpose: Main application entry point.
LW 4 (Task 1) - School Records
Version: 1.0
Author: Yarcev A.A.
Date: 17.04.2026
"""

import models
import storage
import utils

def sort_students_by_name(students):
    """
    Sorts a list of Student objects by name.
    """
    return sorted(students, key=lambda x: x.full_name)

def run_program():
    """Main program loop providing the user interface."""
    db_list = [
        {"full_name": "Smith J.A.", "day": 15, "month": 3, "year": 2006},
        {"full_name": "Doe A.B.", "day": 20, "month": 12, "year": 2006}
    ]

    while True:
        print("\n--- School Management System ---")
        print(f"Total student objects created in session: {models.Student.total_students}")
        print("1. Save current list to files (CSV & Pickle)")
        print("2. Load from file, Sort and Search by Month")
        print("3. Add new Student")
        print("4. Exit")
        
        choice = utils.get_int_input("Action: ", 1, 4)

        if choice == 1:
            storage.save_to_csv("data.csv", db_list)
            storage.save_to_pickle("data.pkl", db_list)
            print(f"Saved {len(db_list)} records to files.")

        elif choice == 2:
            loaded_data = storage.load_from_pickle("data.pkl")
            if not loaded_data:
                print("No data loaded from file.")
                continue
            
            db_list = loaded_data 
            
            models.Student.total_students = 0
            student_objects = []
            for item in db_list:
                try:                                                                                                                                                                                                                        
                    s = models.Student(item['full_name'], int(item['day']), int(item['month']), int(item['year']))
                    student_objects.append(s)
                except (ValueError, KeyError) as e:
                    print(f"Data error: {e}")

            sorted_students = sort_students_by_name(student_objects)
            
            search_m = utils.get_int_input("Enter birth month to filter (1-12): ", 1, 12)
            print(f"\nStudents born in month {search_m}:")
            found = False
            for s in sorted_students:
                if s.month == search_m:
                    print(s)
                    found = True
            if not found:
                print("No students found for this month.")

        elif choice == 3:
            name = utils.get_non_empty_string("Enter Surname and Initials: ")
            d = utils.get_int_input("Day: ", 1, 31)
            m = utils.get_int_input("Month: ", 1, 12)
            y = utils.get_int_input("Year: ", 1990, 2026) 
            
            try:
                new_student = models.Student(name, d, m, y)
                db_list.append(new_student.to_dict())
                print("Student added to the current session.")
            except ValueError as e:
                print(f"Validation Error: {e}")

        elif choice == 4:
            print("Program terminated.")
            break

if __name__ == "__main__":
    try:
        run_program()
    except KeyboardInterrupt:
        print("\nForce closed by user.")