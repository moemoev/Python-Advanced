import sys
from io import StringIO

# input1 = """5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
# """
# input2 = """2
# KK
# KK
# """
# input3 = """8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
# """
# sys.stdin = StringIO(input2)

n = int(input())
board = []
count_removed_knights = 0
max_count_knights = 0
max_knight_pos = tuple()
no_atacks_possible = False
# note we will try to run through the matrix and just check if there are knights with other nknights in sigth and remove them one by one

for row in range(n):
    board.append([])
    line = [el for el in input()]
    for col in range(n):
        symbol = line[col]
        board[row].append(symbol)


#  initialization can be shorter


# check if coords are in bounds
def coords_valid(coords: tuple):
    if 0 <= coords[0] <= n - 1 and 0 <= coords[1] <= n - 1:
        return True
    return False


def detect_knights_in_sight(knight_pos: tuple):
    i, j = knight_pos[0], knight_pos[1]
    count_knights_in_sight = 0
    # check every single atztack position, if coords in bound and knight on spot add pos to the set
    #note looks shit, rework this 'one day'...probably never
    if coords_valid((i - 2, j - 1)) and board[i - 2][j - 1] == 'K':
        count_knights_in_sight += 1
    if coords_valid((i - 1, j - 2)) and board[i - 1][j - 2] == 'K':
        count_knights_in_sight += 1
    if coords_valid((i - 2, j + 1)) and board[i - 2][j + 1] == 'K':
        count_knights_in_sight += 1
    if coords_valid((i - 1, j + 2)) and board[i - 1][j + 2] == 'K':
        count_knights_in_sight += 1
    if coords_valid((i + 2, j - 1)) and board[i + 2][j - 1] == 'K':
        count_knights_in_sight += 1
    if coords_valid((i + 1, j - 2)) and board[i + 1][j - 2] == 'K':
        count_knights_in_sight += 1
    if coords_valid((i + 2, j + 1)) and board[i + 2][j + 1] == 'K':
        count_knights_in_sight += 1
    if coords_valid((i + 1, j + 2)) and board[i + 1][j + 2] == 'K':
        count_knights_in_sight += 1

    return count_knights_in_sight


while not no_atacks_possible:
    for row in range(n):
        for col in range(n):
            current_count = 0
            if board[row][col] == 'K':
                knight = (row, col)
                current_count = detect_knights_in_sight(knight)
            if max_count_knights < current_count:
                max_count_knights = current_count
                max_knight_pos = (row, col)
    if max_count_knights == 0:
        no_atacks_possible = True
    if max_knight_pos:
        board[max_knight_pos[0]][max_knight_pos[1]] = 0
        count_removed_knights += 1
        max_knight_pos = tuple()
        max_count_knights = 0

print(count_removed_knights)
# print(count_removed_knights)
# note this got way to complicated, i cant deb ug it properly, needs a fat rework


'''
TASK:
Chess is the oldest game, but it is still popular these days. For this task, we will use only one chess piece - the Knight. 
A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the 
same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it 
can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until there are no 
knights left that can attack one another. 

Input
On the first line, you will receive integer N - the size of the board
On the following N lines, you will receive strings with "K" and "0"
Output
Print a single integer with the minimum number of knights that need to be removed
'''
