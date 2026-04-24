import sys
from io import StringIO
from time import time


# input1 = """9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4
# """
# input2 = """10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4
# """
# sys.stdin = StringIO(input2)

count_queries = int(input())
stack = []

for _ in range(count_queries):
    query = [el for el in input().split()]
    if query[0] == '1':
        stack.append(int(query[1]))
    elif query[0] == '2' and stack:
        stack.pop()
    elif query[0] == '3'and stack:
        print(max(stack))
    elif query[0] == '4' and stack:
        print(min(stack))
print(f"{', '.join(str(stack.pop()) for _ in range(len(stack)))}")

'''
TASK:
You have an empty stack. You will receive an integer – N. On the next N lines you will receive queries. Each query 
is one of these four types:
'1 {number}' – push the number (integer) into the stack
'2' – delete the number at the top of the stack
'3' – print the maximum number in the stack
'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from the top to the bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"
'''