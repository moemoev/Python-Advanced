import sys
from io import StringIO
from collections import deque
import copy

# input1 = """5 6
# .....P
# ......
# ...B..
# ......
# ......
# ULDDDR"""
# input2 = """4 5
# .....
# .....
# .B...
# ...P.
# LLLLLLLL
# """
# input3 = """5 8
# .......B
# ...B....
# ....B..B
# ........
# ..P.....
# ULLL
# """
# input4 = """5 8
# ........
# ...B....
# ...P....
# ........
# ........
# UUUU
# """

# sys.stdin = StringIO(input4)

rows, cols = [int(el) for el in input().split()]
liar = []
for _ in range(rows):
    liar.append([el for el in input()])

cmd = deque(el for el in input())

player_dead = False
player_escaped = False

# find player starting position
# during initialization of the matrix, we could check all the el and find the P and the B, would increase performance
player_pos = []
for row in range(rows):
    if 'P' not in liar[row]:
        continue
    player_pos.append(row)
    player_pos.append(liar[row].index('P'))

position_by_direction = {
    'U': lambda x, y: [x - 1, y],
    'D': lambda x, y: [x + 1, y],
    'L': lambda x, y: [x, y - 1],
    'R': lambda x, y: [x, y + 1],
}


# check if x/y- coords are out of bounds, first one then other cuz one invalid enough "<" cuz length -1
def is_player_escaped(pos: list):
    if not 0 <= pos[0] < rows:
        return True
    elif not 0 <= pos[1] < cols:
        return True
    return False


# check where the bunnies are on the coords and then call the spread fct
def spread_bunnies(copied_liar):
    """
    processes a deepcopy of a list, so that only the bunny pos of the liar are used not the ones newly added
    :param copied_liar: a deepcopy of liar
    :return:
    """
    for row in range(rows):
        for col in range(cols):
            if copied_liar[row][col] == 'B':
                spread_bunny(row, col)
    return


# depending on the borders of the matrix(escaping index error), spread buns
def spread_bunny(row: int, col: int):
    if not row == 0:
        liar[row - 1][col] = 'B'
    if not row == rows - 1:
        liar[row + 1][col] = 'B'
    if not col == 0:
        liar[row][col - 1] = 'B'
    if not col == cols - 1:
        liar[row][col + 1] = 'B'
    return


def player_died():
    for row in range(rows):
        if 'P' in liar[row]:
            return False
    return True

# use to print every single move brother
def print_liar():
    for row in range(rows):
        print("".join(liar[row]))


while not player_dead and not player_escaped:
    direction = cmd.popleft()
    new_player_pos = position_by_direction[direction](*player_pos)
    if is_player_escaped(new_player_pos):
        liar[player_pos[0]][player_pos[1]] = '.'
        player_escaped = True
    elif not liar[new_player_pos[0]][new_player_pos[1]] == 'B':
        liar[player_pos[0]][player_pos[1]] = '.'
        liar[new_player_pos[0]][new_player_pos[1]] = 'P'
        player_pos = new_player_pos
    else:
        # player moves into bunny and dies adjust position to where he died
        liar[player_pos[0]][player_pos[1]] = '.'
        player_pos = new_player_pos
    spread_bunnies(copy.deepcopy(liar))
    if player_died():
        player_dead = True
    # print_liar()

for row in range(rows):
    print("".join(liar[row]))
if player_escaped:
    print(f"won: {player_pos[0]} {player_pos[1]}")
else:
    print(f"dead: {player_pos[0]} {player_pos[1]}")


'''
TASK:
You come across an old JS Basics teamwork game. It is about bunnies that multiply extremely fast. There's also a player 
that should escape from their lair. You like the game, so you decide to port it to Python because that's your language 
of choice. The last thing left is the algorithm that determines if the player will escape the lair or not.
First, you will receive a line holding integers N and M, representing the lair's rows and columns.
Next, you receive N strings that can consist only of ".", "B", "P". They represent the initial state of the lair. There 
will be only one player. The bunnies are marked with "B", the player is marked with "P", and everything else is free space, 
marked with a dot ".". 
Then you will receive a string with commands (e.g., LRRULUD) - each letter represents the next move of the player:
L - the player should move one position to the left
R - the player should move one position to the right
U - the player should move one position up
D - the player should move one position down
After every step made, each bunny spreads one position up, down, left, and right. If the player moves to a bunny cell or 
a bunny reaches the player, the player dies. If the player goes out of the lair without encountering a bunny, the player wins.
When the player dies or wins, the game ends. All the activities for this turn continue (e.g., all the bunnies spread 
normally), but there are no more turns. There will be no cases where the moves of the player end before he dies or escapes.
In the end, print the final state of the lair with every row on a separate line. On the last line, print either "dead: 
{row} {col}" or "won: {row} {col}". "Row" and "col" are the cell coordinates where the player has died or the last cell 
he has been in before escaping the lair.
Input
On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
On the following N lines, each row is received in the form of a string. The string will contain only ".", "B", "P". All 
strings will be the same length. There will be only one "P" for all the input
On the last line, the directions are received in the form of a string, containing "R", "L", "U", "D"
Output
On the first N lines, print the final state of the bunny lair
On the last line, print:
If the player won - "won: {row} {col}"
If the player dies - "dead: {row} {col}"
'''
