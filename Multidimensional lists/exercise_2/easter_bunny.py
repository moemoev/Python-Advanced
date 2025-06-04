import sys
from io import StringIO

# input1 = """5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0"""
# input2 = """8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22"""
#
# sys.stdin = StringIO(input2)

n = int(input())
field = []
# the coords for the Bunny position in the filed are declared as B_i and B_j for better overview end readibility of the code
B_i, B_j = 0, 0
# initialize the filed and check for letters or digits, convert digits to int()
for row in range(n):
    field.append([])
    line = [int(el) if not el.isalpha() else el for el in input().split(" ")]
    for col in range(n):
        field[row].append(line[col])
        if field[row][col] == 'B':
            B_i, B_j = row, col

row = [el for el in field[B_i]]
col = [field[i][B_j] for i in range(n)]

left_slice_row = row[:B_j]
right_slice_row = row[B_j + 1:]
upper_slice_col = col[0:B_i]
lower_slice_col = col[B_i + 1:]


# slice the slices into smaller slices depending whether there are x'ses
def slice_the_slices(slice: list):
    index_of_x = len(slice)
    for i in range(len(slice)):
        if slice[i] == 'X':
            index_of_x = i
            break
    return slice[0:index_of_x]


left_slice_row = slice_the_slices(left_slice_row[::-1])[::-1]
right_slice_row = slice_the_slices(right_slice_row)
upper_slice_col = slice_the_slices(upper_slice_col[::-1])[::-1]
lower_slice_col = slice_the_slices(lower_slice_col)

slices_by_direction = {
    'up': upper_slice_col,
    'down': lower_slice_col,
    'left': left_slice_row,
    'right': right_slice_row,
}
max_direction = ''
max_sum = 0
for key, value in slices_by_direction.items():
    if max_sum <= sum(value): #note: needed to put it on <= because if only one possible and it was 0 could finish the cycle
        max_sum = sum(value) #note: ALWAYS MIND THE EDGES DUDE!!!
        max_direction = key

print(max_direction)
for i in range(1, len(slices_by_direction[max_direction]) + 1): # the length of the slice saved in dict with key max direction
    if max_direction == 'up':
        print(f"[{B_i - i}, {B_j}]")
    elif max_direction == 'down':
        print(f"[{B_i + i}, {B_j}]")
    elif max_direction == 'left':
        print(f"[{B_i}, {B_j - i}]")
    elif max_direction == 'right':
        print(f"[{B_i}, {B_j + i}]")
print(max_sum)

# print(*row)
# print(*col)
# print(slices_by_direction)
# print(max_direction)
# print(max_sum)

'''
TASK:
Your task is to collect as many eggs as possible for the holiday.
On the first line, you will be given a number representing the size of the field. On the following few lines, you will 
be given a field with:
One bunny - randomly placed in it and marked with the symbol "B"
Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to find out the direction in which the bunny should go in order to collect the maximum number of eggs. The 
directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some 
of the directions, you should not consider the fields after the trap in this direction. For more clarifications, see the 
examples below.
Input
A number representing the size of the field
The matrix representing the field (each position separated by a single space)
Output
The direction which should be considered as best (lowercase)
The field positions from which we are collecting eggs as lists
The total number of eggs collected
'''
