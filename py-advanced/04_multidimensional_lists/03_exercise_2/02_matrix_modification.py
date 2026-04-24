import sys
from io import StringIO

# input1 = """3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END"""
# input2 = """4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END"""
#
# sys.stdin = StringIO(input2)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])


def indexes_are_valid(i: int, j: int):
    if not 0 <= i <= n -1 or not 0 <= j <= n -1:
        return False
    return True


cmd = input()
while not cmd == "END":
    operation, row, col, val = [el for el in cmd.split()]
    row, col, val = int(row), int(col), int(val)
    # operation = cmd[0]    different way (i would prefer this one) to declare vars
    # row, col , val = [int(el) for el in cmd[1:]]
    if not indexes_are_valid(row, col):
        print(f"Invalid coordinates")
        cmd = input()
        continue
    if operation == 'Add':
        matrix[row][col] += val
    else:
        matrix[row][col] -= val
    cmd = input()
for row in range(n):
    print(*matrix[row])

'''
TASK:
Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's 
rows - N. You will get elements for each column on the following N lines, separated with a single space. You 
will be receiving commands in the following format:
"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes 
are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.
'''