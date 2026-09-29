# Plan:
# 1. Keep the existing grade conversion and validation logic unchanged.
# 2. Add a new menu choice: 4 = Exit.
# 3. When the user selects Exit, print a friendly farewell message and stop the program.
# 4. Keep the output preference order as: Letter Grade first, then Percentage.
# 5. Preserve the friendly invalid-input messages already in the helper function.
# ...existing code...

# This function converts a percentage into a letter grade.
# Example: 85 -> "B"
def get_letter_grade(percentage: float) -> str:
    """Map percentage score to standard letter grades."""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


# This function reads a numeric value from the keyboard safely.
# It accepts a blank input only when a default_value is provided.
# If the user enters an invalid value, it shows a friendly message
# and asks whether to try again.
def read_valid_float(
    prompt: str,
    field_name: str,
    default_value=None,
    min_value=None,
    max_value=None
):
    """Read a numeric value safely and allow a blank input to use the default value."""
    while True:
        raw_value = input(prompt).strip()

        # If the user presses Enter and a default value is allowed,
        # use that default instead of causing a ValueError.
        if raw_value == "" and default_value is not None:
            return default_value

        try:
            value = float(raw_value)

            # Check the allowed range, if limits were specified.
            if min_value is not None and value < min_value:
                print(f"Please enter a valid {field_name}. It must be between {min_value} and {max_value}.")
                retry = input("Would you like to try again? (y/n): ").strip().lower()
                if retry != "y":
                    print("Thank you for using the Grade Calculator. Goodbye!")
                    return None
                continue

            if max_value is not None and value > max_value:
                print(f"Please enter a valid {field_name}. It must be between {min_value} and {max_value}.")
                retry = input("Would you like to try again? (y/n): ").strip().lower()
                if retry != "y":
                    print("Thank you for using the Grade Calculator. Goodbye!")
                    return None
                continue

            return value

        except ValueError:
            print(f"Oops! '{raw_value}' is not a valid number for {field_name}.")
            print("Please enter the valid marks to continue.")
            retry = input("Would you like to enter it again? (y/n): ").strip().lower()
            if retry != "y":
                print("Thank you for using the Grade Calculator. Goodbye!")
                return None


# This is the main program logic.
# It handles input, validation, calculation, and output.
def main():
    print("=== Welcome to the Grade Calculator ===")

    # Read the obtained marks.
    obtained = read_valid_float(
        "Enter obtained marks (1-100): ",
        field_name="obtained marks",
        min_value=1,
        max_value=100
    )
    if obtained is None:
        return

    # Read total marks.
    # If the user presses Enter, use the default value of 100.
    total = read_valid_float(
        "Enter total possible marks (1-100, press Enter for default 100): ",
        field_name="total possible marks",
        default_value=100.0,
        min_value=1,
        max_value=100
    )
    if total is None:
        return

    # If obtained marks are greater than total marks, ask the user to enter valid data.
    while obtained > total:
        print("Sorry! Obtained marks cannot be greater than total marks.")
        print("Please enter valid marks to get the grade.")
        obtained = read_valid_float(
            "Enter obtained marks again (1-100): ",
            field_name="obtained marks",
            min_value=1,
            max_value=100
        )
        if obtained is None:
            return

        total = read_valid_float(
            "Enter total possible marks again (1-100, press Enter for default 100): ",
            field_name="total possible marks",
            default_value=100.0,
            min_value=1,
            max_value=100
        )
        if total is None:
            return

    # Calculate the percentage and letter grade.
    percentage = (obtained / total) * 100
    grade = get_letter_grade(percentage)

    # Ask the user which output format they want.
    print("\nSelect your output preference:")
    print("1. Letter Grade")
    print("2. Percentage")
    print("3. Both")
    print("4. Exit")
    choice = input("Enter choice (1, 2, 3, or 4): ").strip()

    # Display the result.
    # For the "Both" option, show letter grade first and percentage second.
    print("\n--- Your Result ---")
    if choice == "1":
        print(f"Letter Grade: {grade}")
    elif choice == "2":
        print(f"Percentage: {percentage:.2f}%")
    elif choice == "3":
        print(f"Letter Grade: {grade}")
        print(f"Percentage: {percentage:.2f}%")
    elif choice == "4":
        print("Thank you for using the Grade Calculator. Goodbye!")
        return
    else:
        print("Invalid option selected. Showing the preferred output order: Letter Grade first, then Percentage.")
        print(f"Letter Grade: {grade}")
        print(f"Percentage: {percentage:.2f}%")

    # Final friendly closing message.
    print("\nThank you for using the Grade Calculator. Goodbye!")


# Run the main program only when this script is executed directly.
if __name__ == "__main__":
    main()