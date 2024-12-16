def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    operations = ["add", "subtract", "multiply", "divide"]
    while True:
        op = input(f"Choose an operation ({', '.join(operations)}): ").lower()
        if op in operations:
            return op
        else:
            print("Invalid operation. Please choose again.")