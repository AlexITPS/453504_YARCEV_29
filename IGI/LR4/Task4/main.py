"""
Purpose: Main entry point to test RegularPolygon class.
LW 4 (Task 4)
Version: 1.0
Author: Yarcev A.A.
Date: 20.04.2026
"""

import shapes
import utils

available_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 
                    'pink', 'brown', 'gray', 'black', 'white', 'gold', 
                    'silver', 'cyan', 'magenta', 'lime', 'navy', 'teal']

def main():
    """Execution logic for shape construction and visualization."""
    print("\n=== Geometric Figure Constructor ===")
    
    n = utils.get_valid_num("Enter number of sides (n >= 3): ", 3, is_int=True)
    a = utils.get_valid_num("Enter side length (a >= 0.1): ", 0.1)
    
    print(f"\nAvailable colors: {', '.join(available_colors)}")
    color = input("Enter fill color: ").strip().lower()
    if color not in available_colors:
        print(f"Invalid color '{color}'. Using 'gold' as default.")
        color = "gold"
    
    text_label = input("Enter text for figure signature: ").strip() or "My Shape"
    
    try:
        polygon = shapes.RegularPolygon(n, a, color)
        
        print("\n[INFO]: " + polygon.get_info())
        
        polygon.draw_and_save(
            vertices=polygon.get_vertices(),
            color=polygon.color_obj.color,
            info=polygon.get_info(),
            label=text_label,
            filename="polygon_result.png"
        )
        
    except Exception as e:
        print(f"[FATAL ERROR]: {e}")

def repeat_program():
    """Repeater for main flow"""
    while True:
        main()
        
        print("\n" + "-"*40)
        again = input("Create another shape? (y/n): ").strip().lower()
        if again != 'y':
            print("Program terminated. Goodbye!")
            break
        print("\n" + "="*40)

if __name__ == "__main__":
    repeat_program()