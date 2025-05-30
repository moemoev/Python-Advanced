import sys
from io import StringIO

# input1 = """3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# """
#
# sys.stdin = StringIO(input1)

n = int(input())

matrix = [[int(el) for el in input().split(", ")] for row in range(n)]
primary_diagonal = []
secondary_diagonal = []
sum_primary = 0
sum_secondary = 0

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    sum_primary += matrix[i][i]
#    can do it like that to use just one loop, tutor showed this so i didnt jus tcopy paste it into my code
#    secondary_diagonal.append(matrix[i][n - 1 - i])

for row in range(n):
    secondary_diagonal.append(matrix[row][n - row - 1])
    sum_secondary += matrix[row][n - row - 1]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum_secondary}")


'''
TASK:
Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a 
comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
'''