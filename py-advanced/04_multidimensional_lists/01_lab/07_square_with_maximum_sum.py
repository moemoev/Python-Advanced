import sys
from io import StringIO

# input1 = """3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# """
# input2 = """2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
# """
#
# sys.stdin = StringIO(input1)

rows, columns = [int(el) for el in input().split(", ")]

matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
sum_max_2x2 = 0
max_matrix = [[0, 0], [0, 0]]


# process the sum of the square matrix, depending on the indexes of the for loop, check if it is max, return if it is
def sum_submatrix(matrix: list, row_i: int, col_i: int, sum_subm: int):
    sum_elements = 0
    for i in range(row_i, row_i + 2):
        for j in range(col_i, col_i + 2):
            sum_elements += matrix[i][j]
    if sum_subm < sum_elements:
        save_max_matrix(matrix, row_i, col_i)
        return sum_elements
    return sum_subm

# while checking the max sum, call this func whether new max is found and safe the el of the max in the apropriate list of list(matrix)
def save_max_matrix(matrix: list, row_i: int, col_i: int):
    for row in range(2):
        max_matrix[row] = matrix[row_i + row][col_i: col_i + 2]

    # max_matrix[0][0] = matrix[row_i][col_i]
    # max_matrix[0][0 + 1] = matrix[row_i][col_i + 1]
    # max_matrix[0 + 1][0] = matrix[row_i + 1][col_i]
    # max_matrix[0 + 1][0 + 1] = matrix[row_i + 1][col_i + 1]


for i in range(rows - 1):
    for j in range(columns - 1):
        sum_max_2x2 = sum_submatrix(matrix, i, j, sum_max_2x2)
for row in range(len(max_matrix)):
    print(*max_matrix[row])
print(sum_max_2x2)

'''
TASK:
Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest sum of its values. 
On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows, you will get elements for each 
column, separated with a comma and a space ", ". 
You should print the found submatrix and the sum of its elements as shown in the examples. 
'''