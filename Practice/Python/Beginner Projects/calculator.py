def enter_number():
      
    try:
        # input numbers
        num1 = int(input("first number: "))
        num2 = int(input("second number: "))
    
        # input operation
        print('operations: 1. add 2. subtract 3. multiply 4. divide')

        operation = int(input("operation: "))
        
    except ValueError:
        print("[error]")
        enter_number()
    
    # call calculate function to operate
    print(calculate(num1, num2, operation))
    


def calculate(num1,num2,operation):
    if operation == 1:
        result = num1 + num2
    elif operation == 2:
        result = num1 - num2
    elif operation == 3:
        result = num1 * num2
    elif operation == 4:
        result = num1 / num2
    else:
        print('error')

    return result
    
enter_number()