import sys
from collections import deque
from io import StringIO


# input1 = """6 3 - 2 1 * 5 /"""
# input2 = """2 2 - 1 *"""
# input3 = """10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *"""
#
# sys.stdin = StringIO(input3)


operation = [el for el in input().split()]
numbers = deque()

arithmetic_expressions = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}

for el in operation:
    if el in arithmetic_expressions:
        result = numbers.popleft()
        while numbers:
            number = numbers.popleft()
            result = arithmetic_expressions[el](result, number)
        numbers.append(result)
    else:
        numbers.append(int(el))
print(numbers.popleft())
