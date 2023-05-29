
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
    
operation = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    available_symbols = operation.keys()
    while True:
        num1 = float(input("What's the first number?: "))
        for item in operation:
            print(item)
        symbol = input("Pick up an operation from the ones above: ")
        if symbol not in available_symbols:
            print("Invalid operation!")
            exit()
            
        num2 = float(input("What's the second number?: "))

        function = operation[symbol]
        global result 
        result = function(num1, num2)

        print(f"{num1} {symbol} {num2} = {result}")
        
        def calculate(n1, n2):
            global result
            again = input(f"Press 'y' to continue calculating with {result}, type 'n' to exit and start again, or 'exit': ").lower()
            if again == "y":
                num1 = result
                symbol = input("Pick up an operation from the ones above: ")
                num2 = float(input("What's the next number?: "))
                function = operation[symbol]
                result = function(num1, num2)
                print(f"{num1} {symbol} {num2} = {result}")    
                calculate(num1, num2) 
            elif again == 'exit':
                exit()
            else:
                calculator()
            
        calculate(num1, num2) 

calculator()