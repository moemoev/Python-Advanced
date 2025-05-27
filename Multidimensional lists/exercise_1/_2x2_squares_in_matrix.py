import sys
from io import StringIO

# input1 = """3 4
# A B B D
# E B B B
# I J B B
# """
# input2 = """2 2
# a b
# c d
# """
# input3 = """5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# """
# sys.stdin = StringIO(input3)

count_square_matrix = 0

rows, columns = [int(el) for el in input().split()]
matrix = [[el for el in input().split()] for row in range(rows)]

for i in range(rows - 1):
    for j in range(columns - 1):
        el = matrix[i][j]
        # if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]
        # works too as a check
        if el == matrix[i][j + 1] and el == matrix[i + 1][j] and el == matrix[i + 1][j + 1]:
            count_square_matrix += 1
print(count_square_matrix)

'''
TASK:
Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the 
matrix's dimensions in format "{rows} {columns}". On the next rows you will receive characters, separated by a single 
space. Print the number of all square matrices you have found.
'''