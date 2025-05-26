import sys
from io import StringIO

# input1 = """3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# """
# sys.stdin = StringIO(input1)

sum_elements = 0
rows, columns = [int(el) for el in input().split(", ")]
matrix = []
for i in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
    sum_elements += sum(matrix[i])
print(sum_elements)
print(matrix)

'''
TASK:
Write a program that reads a matrix from the console and prints:
The sum of all numbers in the matrix
The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows, you will get 
elements for each column separated by a comma and a space ", ". 
'''