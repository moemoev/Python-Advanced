import sys
from io import StringIO

# input1 = """2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
# """
# input2 = """1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
# """
#
# sys.stdin = StringIO(input2)

rows, cols = [int(el) for el in input().split()]
matrix = [[el for el in input().split()] for row in range(rows)]


def not_valid(command: str):
    print("Invalid input!")
    command = input()
    return command


def indexes_valid():
    if not 0 <= row1 < rows and not 0 <= row2 < rows:
        return False
    if not 0 <= col1 < cols and not 0 <= col2 < cols:
        return False
    return True


cmd = input()
while not cmd == 'END':
    cmd_list = [el for el in cmd.split()]
    if not cmd_list[0] == 'swap':
        cmd = not_valid(cmd)
        continue
    if not len(cmd_list) == 5:
        cmd = not_valid(cmd)
        continue
    row1, col1, row2, col2 = map(int, cmd_list[1:])
    if not indexes_valid():
        cmd = not_valid(cmd)
        continue
    matrix[row2][col2], matrix[row1][col1] = matrix[row1][col1], matrix[row2][col2]
    for row in range(rows):
        print(*matrix[row])
    cmd = input()


'''
TASK:
Write a program that reads a matrix, from the console and perform certain operations with its elements. User input is 
provided in a similar way like in the problems above - first you read the dimensions and then the data. 
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and 
("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along 
with four valid coordinates (no more, no less), separated by a single space.
If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus you will 
be able to check if the operation was performed correctly). 
If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered or the given 
coordinates are not valid), print "Invalid input!" and move on to the next command. A negative value makes the coordinates 
not valid. Your program should finish when the command "END" is entered.
'''