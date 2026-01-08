

def add_two_numbers(a, b):
    return a + b

def multiply_two_numbers(a, b):
    return a * b

def minus_two_numbers(a, b):
    return a - b

def power_two_numbers(a, b):
    return a**b

def add_multiply_two_numbers(a,b):
    return add_two_numbers(a, b) + multiply_two_numbers(a, b)

def add_power_two_numbers(a,b):
    return add_two_numbers(a, b) + power_two_numbers(a, b)


def math_operation(a, b, result, test):

    answer = 0

    if test == "add": 
        answer = add_two_numbers(a, b) 
    elif test == "multiply": 
        answer = multiply_two_numbers(a, b) 
    elif test == "minus": 
        answer = minus_two_numbers(a, b) 
    elif test == "power": 
        answer = power_two_numbers(a, b) 
    elif test == "add_multiply": 
        answer = add_multiply_two_numbers(a, b)
    elif test == "add_power": 
        answer = add_power_two_numbers(a, b)
    else: 
        print("No operation")

    return ( result + answer )


def input_check_test(a, b, result):

    running = True

    check = input ("What do I do? ")
    if check == "quit": 
        running = False

    if check == "math": 
        test = input ("What next? ") 
        result = math_operation(a, b, result, test)

    print(f"Current result is {result}.")

    return running, result


def math_test():

    running = True
    result = 0
    a = 3
    b = 4

    while running:

        running, result = input_check_test(a, b, result)
        print("Round we go...")

    return result
