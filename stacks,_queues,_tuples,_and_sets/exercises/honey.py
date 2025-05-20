import sys
from io import StringIO
from collections import deque

# input1 = """20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
# """
# input2 = """30
# 15 9 5 150 8
# * + + * -
# """
# sys.stdin = StringIO(input1)
bees = deque(int(el) for el in input().split())  # stack
nectar = [int(el) for el in input().split()]
honey_operations = deque(input().split())
processed_honey = 0

while bees and nectar:
    if not bees[0] <= nectar[-1]:
        nectar.pop()
        continue
    operation = honey_operations.popleft()
    if operation == '+':
        processed_honey += abs(bees.popleft() + nectar.pop())
    elif operation == '-':
        processed_honey += abs(bees.popleft() - nectar.pop())
    elif operation == '*':
        processed_honey += abs(bees.popleft() * nectar.pop())
    elif operation == '/':
        if nectar[-1] == 0:
            bees.popleft()
            nectar.pop()
            continue
        processed_honey += abs(bees.popleft() / nectar.pop())

print(f"Total honey made: {processed_honey}")
if bees:
    print(f"Bees left:", ', '.join(str(el) for el in bees))
if nectar:
    print(f"Nectar left:", ', '.join(str(el) for el in nectar))
