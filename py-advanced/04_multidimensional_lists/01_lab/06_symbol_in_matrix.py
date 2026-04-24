import sys
from io import StringIO

# input1 = """3
# ABC
# DEF
# X!@
# !
# """
# input2 = """4
# asdd
# xczc
# qwee
# qefw
# 4
# """
# sys.stdin = StringIO(input2)

n = int(input())

matrix = []
for _ in range(n):
    matrix.append([el for el in input()])

symbol = input()
occurs = False
for i in range(n):
    if matrix[i].count(symbol):
        print(f"({i}, {matrix[i].index(symbol)})")
        occurs = True
        break
if not occurs:
    print(f"{symbol} does not occur in the matrix")


'''
TASK:
Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines, you 
will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol. Find the 
first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". You should start 
searching from the top left. If there is no such symbol, print the message "{symbol} does not occur in the matrix".
'''