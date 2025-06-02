import sys
from io import StringIO

# input1 = """4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
# """
# input2 = """5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5
# """
# sys.stdin = StringIO(input2)

rows, columns = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for row in range(rows)]

max_sum = -sys.maxsize
max_submatrix = []
index_max_sum_matrix = (0, 0)

for row in range(rows - 2):
    for column in range(columns - 2):
        # create the submatrix with list compr and list slicing to get a single list and then use sum(), pretty elegant
        submatrix = [el for row in matrix[row:row + 3] for el in row[column:column + 3]]
        sum_submatrix = sum(submatrix)
        if max_sum < sum_submatrix:
            max_sum = sum_submatrix
            index_max_sum_matrix = (row, column)

print(f"Sum = {max_sum}")
for i in range(3):
    print(*matrix[index_max_sum_matrix[0] + i][index_max_sum_matrix[1]:index_max_sum_matrix[1] + 3])


'''
TASK:
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square that has maximal sum of its 
elements. There will be no case with two of more 3x3 squares with equal maximal sum.
Input
On the first line, you will receive the rows and columns in format "{rows} {columns}" – integers in range [1, 20]
On the next lines you will receive each row with its columns - integers, separated by a single space
Output
On the first line print the maximum sum of the elements in the 3x3 square in format "Sum = {sum}"
On the next 3 lines print each element of the found submatrix, separated by a single space
'''