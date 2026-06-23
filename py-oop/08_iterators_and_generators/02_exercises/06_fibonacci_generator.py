def fibonacci():
    a, b = 0, 1
    yield a
    yield b
    while True:
        sum_ab = a + b
        yield sum_ab
        a, b = b, sum_ab

#note more compact but harder to get
# def fibonacci():
#     a, b = -1, 1
#
#     while True:
#         sum_ab = a + b
#         yield sum_ab
#         a, b = b, sum_ab


generator = fibonacci()
for i in range(8):
    print(next(generator))