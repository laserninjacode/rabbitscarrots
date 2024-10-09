def try_int(value):
    # Try to convert the input to an integer, return None if it fails
    try:
        return int(value)
    except ValueError:
        print(f"Error: The value {value} is not a valid integer.")
        value = try_int(input("Try again: "))
        return value

def try_float(value):
    # Try to convert the input to a float, return None if it fails
    try:
        return float(value)
    except ValueError:
        print(f"Error: The value {value} is not a valid float.")
        value = try_float(input("Try again: "))
        return value

def try_string(value):
    # Try to convert the input to a string, return None if it fails
    try:
        return str(value)
    except ValueError:
        print(f"Error: The value {value} is not a valid string.")
        value = try_string(input("Try again: "))
        return value
    
def try_bool(value):
    # Try to convert the input to a boolean, return None if it fails
    try:
        return bool(value)
    except ValueError:
        print(f"Error: The value {value} is not a valid boolean.")
        value = try_bool(input("Try again: "))
        return value
    
def add(n1=0, n2=0):
    # If no arguments are passed, ask for input from the user
    if n1 == 0 and n2 == 0:
        num1 = try_float(input("Enter the first number: "))
        if num1 is None:  # If num1 is invalid, stop and return
            return
        num2 = try_float(input("Enter the number you want to add: "))
        if num2 is None:  # If num2 is invalid, stop and return
            return
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    # If valid arguments are passed, return their sum
    elif n1 is not None and n2 is not None:
        return n1 + n2

def subtract(n1=0, n2=0):
    # If no arguments are passed, ask for input from the user
    if n1 == 0 and n2 == 0:
        num1 = try_float(input("Enter the first number: "))
        if num1 is None:  # If num1 is invalid, stop and return
            return
        num2 = try_float(input("Enter the number you want to subtract: "))
        if num2 is None:  # If num2 is invalid, stop and return
            return
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    # If valid arguments are passed, return their difference
    elif n1 is not None and n2 is not None:
        return n1 - n2

def multiply(n1=0, n2=0):
    # If no arguments are passed, ask for input from the user
    if n1 == 0 and n2 == 0:
        num1 = try_float(input("Enter the first number: "))
        if num1 is None:  # If num1 is invalid, stop and return
            return
        num2 = try_float(input("Enter the number you want to multiply by: "))
        if num2 is None:  # If num2 is invalid, stop and return
            return
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    # If valid arguments are passed, return their product
    elif n1 is not None and n2 is not None:
        return n1 * n2

def divide(n1=0, n2=0):
    # If no arguments are passed, ask for input from the user
    if n1 == 0 and n2 == 0:
        num1 = try_float(input("Enter the first number: "))
        if num1 is None:  # If num1 is invalid, stop and return
            return
        num2 = try_float(input("Enter the number you want to divide by: "))
        # If num2 is invalid or zero, stop and warn the user
        if num2 is None or num2 == 0:
            print("Oh no you don't! Division by zero is not allowed.")
            return
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}.")
    # If valid arguments are passed, ensure num2 is not zero before dividing
    elif n1 is not None and n2 is not None:
        if n2 == 0:
            print("Oh no you don't! Division by zero is not allowed.")
            return None
        return n1 / n2

def remainder(n1=0, n2=0):
    # If no arguments are passed, ask for input from the user
    if n1 == 0 and n2 == 0:
        num1 = try_float(input("Enter the first number: "))
        if num1 is None:  # If num1 is invalid, stop and return
            return
        num2 = try_float(input("Enter the number you want to divide by: "))
        # If num2 is invalid or zero, stop and warn the user
        if num2 is None or num2 == 0:
            print("Oh no you don't! Division by zero is not allowed.")
            return
        result = num1 % num2
        print(f"The remainder of {num1} / {num2} is {result}.")
    # If valid arguments are passed, ensure num2 is not zero before finding remainder
    elif n1 is not None and n2 is not None:
        if n2 == 0:
            print("Oh no you don't! Division by zero is not allowed.")
            return None
        return n1 % n2
