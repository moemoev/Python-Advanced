def add(ints: list):
    return sum(ints)


def sub(ints: list):
    result = ints.pop(0)
    for el in ints:
        result -= el
    return result


def mult(ints: list):
    result = 1
    for el in ints:
        result *= el
    return result


def div(ints: list):
    result = ints.pop(0)
    for el in ints:
        result /= el
    return result


def operate(operator: chr, *args):
    if operator == '+':
        result = add(list(args))
    elif operator == '-':
        result = sub(list(args))
    elif operator == '*':
        result = mult(list(args))
    elif operator == '/':
        result = div(list(args))
    return result


print(operate("*", 3, 4))

'''
TASK:
Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple numbers 
(integers) as additional arguments (*args). The function should return the result of the operator applied to all the 
numbers. For more clarification, see the examples below. 
Submit only your function in the Judge system.
Note: Be careful when you have multiplication and division
'''
