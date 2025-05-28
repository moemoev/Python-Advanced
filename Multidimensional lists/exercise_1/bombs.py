import sys
from io import StringIO
from collections import deque

# input1 = """4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0
# """
# input2 = """3
# 7 8 4
# 3 1 5
# 6 4 9
# 0,2 1,0 2,2
# """
#
# sys.stdin = StringIO(input2)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

values = [el for el in input().split()]
# no idea why they have to be tuples, but i kinda liked it -> might be cuz immutable but "these go to eleven"
# made it a queue afterwards to just popleft data, therefore this step looks like hell or "pythonstyle"
bombs = deque(tuple(map(int, (value.split(",")))) for value in values)

alive_cells = 0
sum_alive_cells = 0

def adjust_bomb_indexes(row: int, col: int):
    # adjust the range of the matrix[slices] to not run into index error
    rowl, rowr, coll, colr = row - 1, row + 1, col - 1, col + 1
    if row - 1 < 0:
        rowl = 0
    if col - 1 < 0:
        coll = 0
    if row + 1 >= n:
        rowr = n - 1
    if col + 1 >= n:
        colr = n - 1
    return rowl, rowr, coll, colr


def dmg(rl: int, rr: int, cl: int, cr: int, damage: int):
    # process dmg done whether val is >0
    for i in range(rl, rr + 1):
        for j in range(cl, cr + 1):
            if 0 < matrix[i][j]:
                matrix[i][j] -= damage
    return

def count_alive_cells(count_cells: int,sum_cells: int ):
    for row in range(n):
        for col in range(n):
            if 0 < matrix[row][col]:
                sum_cells += matrix[row][col]
                count_cells += 1
    return count_cells, sum_cells

while bombs:
    bomb_row, bomb_col = bombs.popleft()
    if not matrix[bomb_row][bomb_col] <= 0:
        bomb_val = matrix[bomb_row][bomb_col]
        bomb_row_l, bomb_row_r, bomb_col_l, bomb_col_r = adjust_bomb_indexes(bomb_row, bomb_col)
        dmg(bomb_row_l, bomb_row_r, bomb_col_l, bomb_col_r, bomb_val)
        matrix[bomb_row][bomb_col] = 0
alive_cells, sum_alive_cells = count_alive_cells(alive_cells, sum_alive_cells)

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cells}")

for row in range(n):
    print(*matrix[row])

'''
TASK:
You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new 
line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single space, in 
the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells there are bombs. You must detonate every bomb, in the order they were given. When a bomb explodes, it deals 
damage equal to its own integer value, to all the cells around it (in every direction and in all diagonals). One bomb can't 
explode more than once and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells 
can't explode.
You must print the count of all alive cells and their sum. Afterwards, print the matrix with all its cells (including the 
dead ones).
Input
On the first line, you are given the integer N - the size of the square matrix.
The next N lines holds the values of each column - N numbers separated by a space.
On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
Output
On the first line, you need to print the count of all alive cells in the format: 
"Alive cells: {alive_cells}"
On the second line, you need to print the sum of all alive cell in the format: 
"Sum: {sum_of_cells}"
In the end print the matrix. The cells must be separated by a single space.
'''