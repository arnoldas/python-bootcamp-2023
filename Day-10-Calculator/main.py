import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# !!! This function wouldn't be called
# def calculation_function(n1, n2):
#     print("testing")
#     return 0

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    
    for symbol in operations:
        print(symbol)
    
    continue_calculating = True
    while continue_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        #Or it can be achived in one line of code:
        #answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input(
                f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: "
        ) == "y":
            num1 = answer
        else:
            continue_calculating = False
        calculator()
calculator()