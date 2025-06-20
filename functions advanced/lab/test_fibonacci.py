# Fibonacci
# f(n) = f(n-1) + f(n-2)
# f(1) = f(0) = 1
#

def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) # starts to split at every lvl which results into a tree, therefore printing looks awkward

print(fibonacci(6))