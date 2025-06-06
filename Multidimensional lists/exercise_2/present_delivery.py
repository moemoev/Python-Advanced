import sys
from io import StringIO

# input1 = """5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning"""
# input2 = """3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up"""

# sys.stdin = StringIO(input2)

count_presents = int(input())
no_more_presents = False
n = int(input())

matrix = []
santa = (0, 0)
count_nais_kids = 0 #  kids who could get a present
count_happy_kids = 0 # kids who did get a present

for row in range(n):
    matrix.append([])
    inline = [el for el in input().split(" ")]
    for col in range(n):
        matrix[row].append(inline[col])
        if matrix[row][col] == 'S':
            santa = (row, col)
        elif matrix[row][col] == 'V':
            count_nais_kids += 1

new_position_by_direction={
    'up':lambda x, y: (x - 1, y),
    'down':lambda x, y: (x + 1, y),
    'left':lambda x, y: (x, y - 1),
    'right':lambda x, y: (x, y + 1),
}


def move_is_valid(new_pos: tuple):
    i, j = new_pos[0], new_pos[1]
    if 0 <= i < n and 0 <= i < n:
        return True
    return False


def move_santa(pos: tuple, direction: str):
    i, j = pos[0],pos[1]
    if new_position_by_direction[direction](i, j):
        matrix[i][j] = '-'
        pos = new_position_by_direction[direction](i, j)
    return pos

# up, down, left, right
def cookie_time(pos: tuple, present: int, count_kids: int):
    i, j = pos[0], pos[1]
    #possible_moves = [(-1, 0),(+1, 0), (0, -1), (0, +1)]
    viable_moves= []
    for direction in new_position_by_direction:
        if move_is_valid(new_position_by_direction[direction](i, j)):
            viable_moves.append(new_position_by_direction[direction](i, j))
    present, count_kids = work_fields_around(viable_moves, present, count_kids)
    return present, count_kids

def work_fields_around(moves: list, present: int, count_kids: int):
    for move in moves:
        i, j = move[0], move[1]
        if matrix[i][j] == 'V':
            count_kids += 1
            present -= 1
            matrix[i][j] = '-'
        elif matrix[i][j] == 'X':
            present -= 1
            matrix[i][j] = '-'
        if present == 0:
            break
    return present, count_kids

cmd = input()
while not cmd == 'Christmas morning':
    matrix[santa[0]][santa[1]] = '-'
    santa = move_santa(santa, cmd)
    i, j = santa[0], santa[1]
    if matrix[i][j] == 'V':
        count_presents -= 1
        count_happy_kids += 1
        matrix[i][j] = '-'
    elif matrix[i][j] == 'X':
        matrix[i][j] = '-'
    elif matrix[i][j] == 'C':
        count_presents, count_happy_kids = cookie_time((i,j), count_presents, count_happy_kids)
    matrix[i][j] = 'S'
    if count_presents == 0:
        no_more_presents = True
        break
    cmd = input()

if no_more_presents and not count_happy_kids == count_nais_kids:
    print(f"Santa ran out of presents!")
for row in range(n):
    print(*matrix[row])
if count_happy_kids == count_nais_kids:
    print(f"Good job, Santa! {count_nais_kids} happy nice kid/s.")
else:
    print(f"No presents for {count_nais_kids - count_happy_kids} nice kid/s.")


'''
TASK:
The presents are ready, and Santa has to deliver them to the kids. 
You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood 
with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood. 
Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live. If the 
cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V". 
There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive. 
If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid, he 
doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and 
extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or nice).
 If Santa has been to a house, the cell becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to these 
cells, or if he does, he returns to the cell where the cookie was.
If Santa runs out of presents or receives the command "Christmas morning", you should end the program. 
Keep in mind that you should check whether all the nice kids received presents.
Input
On the first line, you are given the integer m - the count of presents
On the second - integer n - the size of the neighborhood
The following n lines hold the values for every row
On each of the following lines you will get a command
Output
On the first line:
If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
Next, print the matrix.
In the end, print one of these messages:
If he manages to give all the nice kids presents, print:
"Good job, Santa! {count_nice_kids} happy nice kid/s."
Otherwise, print: 
"No presents for {count nice kids} nice kid/s."
'''