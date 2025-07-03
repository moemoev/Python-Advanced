def fib(n):
    stream = [0, 1]
    [stream.append(stream[i - 2] + stream[i - 1]) for i in range(2, n)]
    return stream


print(fib(10))
