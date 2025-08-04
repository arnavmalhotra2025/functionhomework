import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Radius cannot be negative.")
        else:
            result = calculate_circumference(radius)
            print(f"The circumference is: {result:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

main()