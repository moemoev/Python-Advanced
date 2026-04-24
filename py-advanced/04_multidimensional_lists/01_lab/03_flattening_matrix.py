import sys
from io import StringIO

# input1 = """2
# 1, 2, 3
# 4, 5, 6
# """
# input2 = """3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
# """
#
# sys.stdin = StringIO(input2)

rows = int(input())
matrix = [[int(el) for el in input().split(", ")]for row in range(rows)]
flattened_matrix = []
for row in range(rows):
    flattened_matrix += matrix[row]
print(flattened_matrix)


'''
TASK:
Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example, 
the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for each 
column separated with a comma and a space ", ".
'''