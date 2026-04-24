#Factorial
# f(n) = f(n-1) * n
# f(0) = 1
# f(1) = 1

# we do set f(0) as return 1 since f(1) n is already n, the value we do return
def factorial(number: int):
    if number == 0:  # using if number == 0 or number == 1 would spare one fct call which would increase performance but i dont care
        return 1
    return factorial(number - 1) * number


print(factorial(8))
