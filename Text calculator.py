import re
def calculate(expression):
    """
    Evaluates a basic arithmetic expression and returns the result.

    :param expression: A string containing the arithmetic expression.
    :return: The result of the calculation or an error message.
    """
    try:
        # Use eval safely by restricting built-in functions
        result = eval(expression, {"__builtins__": {}}, {})
        if isinstance(result, (int, float)):
            return result
        else:
            raise ValueError("Invalid operation.")
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: Invalid input. Details: {e}"


def main():
    """
    Main function to run the calculator program.
    """
    print("Welcome to the Text-Based Calculator!")
    print("You can perform basic operations: addition (+), subtraction (-), multiplication (*), division (/).")
    print("Type 'exit' to quit the calculator.\n")

    while True:
        # Get user input
        user_input = input("Enter an expression: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Validate and calculate
        if re.match(r'^[0-9+\-*/().\s]+$', user_input):
            result = calculate(user_input)
            print(f"Result: {result}")
        else:
            print("Error: Invalid input. Please use numbers and valid operators (+, -, *, /).")

if __name__ == "__main__":
    main()
