import sys
from io import StringIO

# input1 = """5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left"""
# input2 = """7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right"""
#
# sys.stdin = StringIO(input2)

alice = (-1, -1)
rabit_i, rabit_j = -1, -1
n = int(input())
field = []
collected_tea = 0

# initialize the field and get the positions of A and R and convert numbers_in_one_line.txt to ints
for row in range(n):
    field.append([])
    input_line = [el for el in input().split(" ")]
    for col in range(n):
        if input_line[col].isdecimal():
            field[row].append(int(input_line[col]))
        else:
            field[row].append(input_line[col])
            if field[row][col] == 'A':
                alice = (row, col)
            elif field[row][col] == 'R':
                rabit_i, rabit_j = row, col

coords_by_directions = {
    'up': lambda x: (x[0] - 1, x[1]),
    'down': lambda x: (x[0] + 1, x[1]),
    'left': lambda x: (x[0], x[1] - 1),
    'right': lambda x: (x[0], x[1] + 1),
}


def inside_wonderland(alice: tuple):
    for i in range(len(alice)):
        if not 0 <= alice[i] < n:
            return False
    return True


game_over = False
cmd = input()
while collected_tea < 10:
    field[alice[0]][alice[1]] = '*'
    alice = coords_by_directions[cmd](alice)
    if not inside_wonderland(alice):
        game_over = True
        break
    if field[alice[0]][alice[1]] == 'R':
        field[alice[0]][alice[1]] = '*'
        game_over = True
        break
    if not field[alice[0]][alice[1]] == '.' and not field[alice[0]][alice[1]] == '*':
        collected_tea += field[alice[0]][alice[1]]
        field[alice[0]][alice[1]] = '*'
        if 10 <= collected_tea:
            break
    cmd = input()

if game_over:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")
for row in range(n):
    print(*field[row])


'''
TASK:
Alice is going to the mad tea party, to see her friends. On the way to the party she needs to collect bags of tea.
You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, 
you will receive the rows of the territory:
Alice will be placed in a random position, marked with the letter "A". 
On the territory there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects 
the tea bags and increases the quantity with the corresponding number.
There will always be one rabbit hole on the territory marked with the letter "R".
All of the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue 
collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends. 
In the end, all the path she walked has to be marked with '*'.
For more clarifications, see the examples below.
Input
On the first line, you will be given the integer n – the size of the square matrix
On the following n lines - matrix representing the field (each position separated by a single space)
On each of the following lines you will be given a move command
Output
On the first line: 
If Alice steps on the rabbit hole or she go out of the territory, print: 
"Alice didn't make it to the tea party."
If she collected at least 10 bags of tea, print: 
"She did it! She went to the party."
On the following lines, print the matrix.
'''