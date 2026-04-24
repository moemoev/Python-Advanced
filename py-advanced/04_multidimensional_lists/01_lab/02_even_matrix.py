import sys
from io import StringIO

# input1 = """2
# 1, 2, 3
# 4, 5, 6
# """
# input2 = """4
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67
# """
#
# sys.stdin = StringIO(input1)

rows = int(input())
matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in  range(rows)]

# for _ in range(rows):
#     matrix.append([int(el) for el in input().split(", ")])
print(matrix)

'''
TASK:
Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use nested 
comprehension for that problem. 
On the first line, you will receive the rows of the matrix. On the next rows, you will get elements for each column 
separated with a comma and a space ", ".  
'''