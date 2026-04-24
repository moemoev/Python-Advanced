import sys
from io import StringIO

# input1 = """3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# """
# input2 = """3, 3
# 1 2 3
# 4 5 6
# 7 8 9
# """
#
# sys.stdin = StringIO(input2)

rows,columns = [int(el) for el in input().split(", ")]


matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for column in range(columns):
    sum_columns = 0
    for row in range(rows):
        sum_columns += matrix[row][column]
    print(sum_columns)


'''
TASK:
Write a program that reads a matrix from the console and prints the sum for each column on separate lines. 
On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for 
each column separated with a single space. 
'''