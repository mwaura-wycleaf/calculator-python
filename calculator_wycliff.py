
# --- Arithmetic operation functions ---

def add(a, b):
    # Returns the sum of a and b
    return a + b

def subtract(a, b):
    # Returns the difference between a and b
    return a - b

def multiply(a, b):
    # Returns the product of a and b
    return a * b

def divide(a, b):
    # Handles division and prevents division by zero
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

# --- Input validation function ---

def get_number(prompt, memory):
    """
    Prompts the user to enter a number.
    If the user enters 'M', uses the stored memory value.
    Keeps prompting until a valid number or 'M' is entered.
    """
    while True:
        value = input(prompt)
        if value.upper() == 'M':
            if memory is None:
                print("Memory is empty!")
                continue
            return memory
        try:
            return float(value)
        except ValueError:
            print("Invalid input! Please enter a number or 'M' for memory.")

# --- Main calculator logic ---

def calculator():
    memory = None     # Stores the last saved result
    history = []      # List to track the last 5 calculations

    while True:
        # Display main menu
        print("\n=== Simple Calculator ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        print("6. Memory Functions (M+, MR, MC)")
        print("7. View History")

        choice = input("Choose operation (1-7): ")

        # Exit the program
        if choice == '5':
            print("Thank you for using the calculator!")
            break

        # Handle memory functions
        elif choice == '6':
            print("\n--- Memory Functions ---")
            print("1. Store (M+)")
            print("2. Recall (MR)")
            print("3. Clear (MC)")
            mem_choice = input("Choose memory option (1-3): ")

            if mem_choice == '1':
                # Store a number to memory
                result = get_number("Enter value to store in memory: ", memory)
                memory = result
                print(f"Memory stored: {memory}")
            elif mem_choice == '2':
                # Recall memory value
                print(f"Memory: {memory if memory is not None else 'Empty'}")
            elif mem_choice == '3':
                # Clear memory
                memory = None
                print("Memory cleared.")
            else:
                print("Invalid memory option.")

        # View or clear calculation history
        elif choice == '7':
            print("\n--- History ---")
            if not history:
                print("No history available.")
            else:
                for i, item in enumerate(history[-5:], start=1):
                    print(f"{i}. {item}")
            clear = input("Clear history? (y/n): ").lower()
            if clear == 'y':
                history.clear()
                print("History cleared.")

        # Perform arithmetic operations
        elif choice in ['1', '2', '3', '4']:
            # Get two numbers, with memory recall option
            num1 = get_number("Enter first number (or 'M' for memory): ", memory)
            num2 = get_number("Enter second number (or 'M' for memory): ", memory)

            # Perform the selected operation
            if choice == '1':
                result = add(num1, num2)
                op = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op = '/'

            # Display result and save to history if successful
            if isinstance(result, str):
                # Error case (e.g. divide by zero)
                print(result)
            else:
                # Valid result
                expression = f"{num1} {op} {num2} = {result}"
                print(f"Result: {expression}")
                history.append(expression)

                # Limit history to 5 most recent items
                if len(history) > 5:
                    history.pop(0)

                # Ask user to store result in memory
                save = input("Save result to memory? (y/n): ").lower()
                if save == 'y':
                    memory = result
                    print("Result saved to memory.")

        else:
            # Invalid menu choice
            print("Invalid choice! Please select a number between 1 and 7.")

        # Ask if user wants to continue
        cont = input("Continue? (y/n): ").lower()
        if cont != 'y':
            print("Thank you for using the calculator!")
            break

# --- Entry Point: Call calculator() only if file is run directly ---
if __name__ == "__main__":
    calculator()