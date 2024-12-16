from calculator import add, subtract, multiply, divide
from operations import get_float_input, get_operation

def main():
    print("Welcome to the Simple Calculator!")
    num1 = get_float_input("Enter the first number: ")
    num2 = get_float_input("Enter the second number: ")
    operation = get_operation()

    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        else:
            result = None
        
        print(f"The result of {operation} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()