# don't forget that 0! is 1, so if n == 1 is not enough !
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(1))
