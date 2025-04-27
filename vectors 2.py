import math
import os

# Theme settings
print("Choose a Theme:")
print("1. Light Mode")
print("2. Dark Mode")
theme = input("Enter 1 or 2: ")

if theme == "1":
    text_color = "\033[30m"  # Black text
    bg_color = "\033[47m"    # White background
elif theme == "2":
    text_color = "\033[37m"  # White text
    bg_color = "\033[40m"    # Black background
else:
    text_color = "\033[0m"
    bg_color = "\033[0m"

# Start Program
print(bg_color + text_color)
print("\n=== Vector Magnitude, Direction and Quadrant Calculator ===\n")

# Open a file to save results
file = open("vector_results.txt", "w")

while True:
    print("\nMenu:")
    print("1. Solve a Vector")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # Clear screen
        os.system('clear' if os.name == 'posix' else 'cls')

        print("\n=== New Vector Calculation ===\n")
        try:
            x = float(input("Enter x-component: "))
            y = float(input("Enter y-component: "))
        except ValueError:
            print("\nInvalid input! Please enter numbers only.")
            continue

        # Calculate magnitude
        magnitude = math.sqrt(x**2 + y**2)

        # Calculate direction
        angle_rad = math.atan2(y, x)
        angle_deg = math.degrees(angle_rad)

        # Make sure direction is positive
        if angle_deg < 0:
            angle_deg += 360

        # Find Quadrant
        if x > 0 and y > 0:
            quadrant = "Quadrant 1"
        elif x < 0 and y > 0:
            quadrant = "Quadrant 2"
        elif x < 0 and y < 0:
            quadrant = "Quadrant 3"
        elif x > 0 and y < 0:
            quadrant = "Quadrant 4"
        elif x == 0 and y != 0:
            quadrant = "On Y-Axis"
        elif y == 0 and x != 0:
            quadrant = "On X-Axis"
        else:
            quadrant = "At the Origin"

        # Display results
        print("\nResults:")
        print(f"Magnitude: {round(magnitude, 2)}")
        print(f"Direction: {round(angle_deg, 2)} degrees")
        print(f"Quadrant: {quadrant}")

        # Save results to file
        file.write(f"Vector (x={x}, y={y}) -> Magnitude: {round(magnitude,2)}, Direction: {round(angle_deg,2)} degrees, {quadrant}\n")

    elif choice == "2":
        print("\nExiting Program...")
        break
    else:
        print("\nInvalid choice. Please enter 1 or 2.")

# Close the file
file.close()

# Show saved results
print("\nHere are all your vector results:")
with open("vector_results.txt", "r") as file:
    print(file.read())

# Reset colors
print("\033[0m")