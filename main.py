"""
    program name:  Geometric calculator
    Author: Adhanet Gebretensay
    Purpose: Menu driven geometric calculator
    Starter Code: None
    Date: 09/20/2026
"""
import circle as c
import rectangle as r 

# Aliases are used because we want to avoid name collision. 
# The function calc_area() has the same name in both modules, so we have to use aliases.



def get_number():
    number = float(input())

    while number <= 0:
        print("Please enter a positive number")
        number = float(input())

    return number


def main():
    while True:
        print("Geometry Calculator")
        print("1. Calculate Circle Area")
        print("2. Calculate Circle Circumference")
        print("3. Calculate Rectangle Area")
        print("4. Calculate Rectangle Perimeter")
        print("5. Exit")

        choice = input("\nEnter your choice  ")

        if choice == '1':
            print("Please enter the radius")
            radius = get_number()
            area = c.calc_area(radius)
            print(f"The area is {area:.2f}")

        elif choice == '2':
            print("Please enter the radius")
            radius = get_number()
            circumference = c.calc_circumference(radius)
            print(f"The cirumference is {circumference:.2f}")

        elif choice == '3':
            print("Please enter the width")
            width= get_number()
            print("Please enter the height")
            height= get_number()
            area = r.calc_area(width, height)
            print(f"The area is {area:.2f}")

        elif choice == '4':
            print("Please enter the width")
            width= get_number()
            print("Please enter the height")
            height= get_number()
            perimeter = r.calc_perimeter(width, height)
            print(f"The perimeter is {perimeter:.2f}")

        elif choice == '5':
            print("\nThank you for using the calculator") 
            break

        else:
             print("\nIncorrect choice. Please enter a number 1-5  ")


        input ("\nPress Enter to continue  ")




if __name__ == "__main__":
     main()