import sys
from io import StringIO

# input1 = """4 6"""
# input2 = """3 2"""
#
# sys.stdin = StringIO(input1)

rows, cols = [int(el) for el in input().split()]
matrix = []
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(chr(97 + row) + chr(97 + row + col) + chr(97 + row))
for row in range(rows):
    print(*matrix[row])


'''
TASK:
Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in 
the examples below.
Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
Columns + rows define the middle letter: 
column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
Input
The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
r and c are integers in range [1, 26]
'''