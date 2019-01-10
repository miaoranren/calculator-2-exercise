"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    response = input("> ")
    tokens = response.split(' ')
    
    if tokens[0] == 'q':
        print("You will exit!")
        break
    elif len(tokens) < 2:
        print("Not enough inputs")
        continue
    operator = tokens[0]
    num1 = tokens[1]
    #This is the case with only two index , we default num2 as None.
    if len(tokens) < 3:
        num2 = None
    else:
        num2 = tokens[2]

    result = None   
    if not num1.isdigit()  or num2.isdigit() :
        print("There are not numbers!")
        break
    
    
    elif operator == "+":
        result = add(float(num1),float(num2))

    elif operator == "-":
        result = subtract(float(num1),float(num2))

    elif operator == "*":
        result = multiply(float(num1),float(num2))

    elif operator == "/":
        result = divide(float(num1),float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "pow":
        result = power(float(num1),float(num2))

    elif operator == "mod":
        result = mod(float(num1),float(num2))

    else:
        print('Please enter two integers!')
    
    
    
    

    print(result)


