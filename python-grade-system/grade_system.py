try:
    # Ask the user to enter the mark
    mark = float(input("Enter your mark (0-100): "))

    # Check whether the mark is within the valid range
    if mark < 0 or mark > 100:
        print("Invalid input! Please enter a mark between 0 and 100.")

    # Determine the grade
    elif mark >= 90:
        print(f"Mark: {mark} -> Grade: A")

    elif mark >= 80:
        print(f"Mark: {mark} -> Grade: B")

    elif mark >= 70:
        print(f"Mark: {mark} -> Grade: C")

    elif mark >= 60:
        print(f"Mark: {mark} -> Grade: D")

    else:
        print(f"Mark: {mark} -> Grade: E")

except ValueError:
    print("Invalid input! Please enter a numeric value.")