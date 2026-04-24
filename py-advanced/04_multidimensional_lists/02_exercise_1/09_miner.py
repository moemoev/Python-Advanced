import sys
from io import StringIO
from collections import deque

# input1 = """5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *
# """
# input2 = """4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *
#
# """
# input3 = """6
# left left down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *
# """
#
# sys.stdin = StringIO(input3)

n = int(input())
cmd = deque(el for el in input().split())

field = []
collected_coal = 0
total_coal = 0
position = [-1, -1]
game_over = False
for row in range(n):
    field.append([el for el in input().split()])
# find start coordinates and count total_coal
for row in range(n):
    if 's' in field[row]:
        i = row
        j = field[row].index('s')
        position = [i, j]
    if 'c' in field[row]:
        total_coal += field[row].count('c')

coord_by_direction = {
    'left': lambda x, y: [x, y - 1] if y > 0 else [x, y],
    'up': lambda x, y: [x - 1, y] if x > 0 else [x, y],
    'right': lambda x, y: [x, y + 1] if y < n - 1 else [x, y],
    'down': lambda x, y: [x + 1, y] if x < n - 1 else [x, y],
}

while cmd:
    direction = cmd.popleft()
    position = coord_by_direction[direction](*position)
    if field[position[0]][position[1]] == 'c':
        collected_coal += 1
        field[position[0]][position[1]] = '*'
    elif field[position[0]][position[1]] == 'e':
        game_over = True
        break

if game_over:
    print(f"Game over! ({position[0]}, {position[1]})")
elif collected_coal == total_coal:
    print(f"You collected all coal! ({position[0]}, {position[1]})")
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({position[0]}, {position[1]})")


'''
TASK:
You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move. 
On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible 
commands are "left", "right", "up" and "down". 
In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the 
screen are:
* - a regular position on the field
e - the end of the route
c - coal
s - miner
The miner starts moving from the position "s". He should perform the given commands successively, moving with only one 
position in the given direction. If the miner has reached the edge of the field and the following command indicates that 
he has to get out of the area, he must remain in his current position and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you 
should print whether the miner has succeeded in collecting the coal or not and his final position:
If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected 
all coal! ({row_index}, {col_index})".
If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! 
({row_index}, {col_index})".
If there are no more commands and none of the above cases had happened, you should print the message: 
"{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
Input
Field size - an integer number
Commands to move the miner - a sequence of directions, separated by a single whitespace (" ")
The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
Output
There are three types of output as mentioned above.
'''