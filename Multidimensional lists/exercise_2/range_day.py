import sys
from io import StringIO

# input1 = """. . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1"""
#
# input2 = """. . . . .
# . . . . .
# . A x . .
# . . . . .
# . x . . .
# 2
# shoot down
# shoot right"""
#
# sys.stdin = StringIO(input2)

n = 5

pos = (0, 0)
targets_hit = []
count_targets = 0
field = []
complete = False

for row in range(n):
    field.append([])
    input_line = [el for el in input().split(" ")]
    for col in range(n):
        field[row].append(input_line[col])
        if field[row][col] == 'A':
            pos = (row, col)
        elif field[row][col] == 'x':
            count_targets += 1


def new_pos_in_range(coords: tuple):
    # test whether indexes are in range, here i used n instead of 5, hardcoding kinda doesn't look fitting
    i, j = coords[0], coords[1]
    if 0 <= i < n and 0 <= j < n:
        return True
    return False


def new_pos_is_viable(pos: tuple):
    i, j = pos[0], pos[1]
    if field[i][j] == '.':
        return True
    return False


def move(direct: str, range: int, pos: tuple):
    """test for direction and if new possible coords are in range, and new pos is '.'
    i know three statements in a 'if-cond' looks alot but indenting 4 times looks way worse
    if al tests fail, return the former pos -> shooter does not move """
    i, j = pos[0], pos[1]
    if direct == 'up' and new_pos_in_range((i - range, j)) and new_pos_is_viable((i - range, j)):
        field[i][j] = '.'
        field[i - range][j] = 'A'
        return i - range, j
    elif direct == 'down' and new_pos_in_range((i + range, j)) and new_pos_is_viable((i + range, j)):
        field[i][j] = '.'
        field[i + range][j] = 'A'
        return i + range, j
    elif direct == 'left' and new_pos_in_range((i, j - range)) and new_pos_is_viable((i, j - range)):
        field[i][j] = '.'
        field[i][j - range] = 'A'
        return i, j - range
    elif direct == 'right' and new_pos_in_range((i, j + range)) and new_pos_is_viable((i, j + range)):
        field[i][j] = '.'
        field[i][j + range] = 'A'
        return i, j + range
    return i, j


def shoot(direct: str, pos: tuple):
    i, j = pos[0], pos[1]
    """call shoot_direction with the slice that cointains the pos of the shooter so that returning indexes from the slices of the appearance of X
    does not have to be adjusted-> [A,1,2,x] will return pos 3, so x is 3 pos awys from A"""
    column_as_list = [el for row in range(n) for el in field[row][j]]
    if direct == 'up':
        upper_slice = column_as_list[:i + 1]
        if shoot_slice(upper_slice[::-1]):
            i -= shoot_slice(upper_slice[::-1])
            targets_hit.append((i, j))
            field[i][j] = '.'
    elif direct == 'down':
        lower_slice = column_as_list[i:]
        if shoot_slice(lower_slice):
            i += shoot_slice(lower_slice)
            targets_hit.append((i, j))
            field[i][j] = '.'
    elif direct == 'left':
        left_slice = field[i][:j + 1]
        if shoot_slice(left_slice[::-1]):
            j -= shoot_slice(left_slice[::-1])
            targets_hit.append((i, j))
            field[i][j] = '.'
    elif direct == 'right':
        right_slice = field[i][j:]
        if shoot_slice(right_slice):
            j += shoot_slice(right_slice)
            targets_hit.append((i, j))
            field[i][j] = '.'
    return


def shoot_slice(slice: list):
    """called with the reversed list so that count returns the first occurence of 'x'
    if 'x' exists in this slice, return the pos, othewise 0, so that we can use the val to if-condition it in fct. shoot
    """
    if slice.count('x'):
        pos_x = slice.index('x')
        return pos_x
    return 0


n_cmd = int(input())
for _ in range(n_cmd):
    cmd = [el for el in input().split(" ")]
    command, direction = cmd[0], cmd[1]
    if command == 'move':
        steps = int(cmd[2])
        pos = move(direction, steps, pos)
    elif command == 'shoot':
        shoot(direction, pos)
    if count_targets == len(targets_hit):
        complete = True
        break

if complete:
    print(f"Training completed! All {count_targets} targets hit.")
else:
    print(f"Training not completed! {count_targets - len(targets_hit)} targets left.")

for el in targets_hit:
    print(list(el))


'''
TASK:
You are participating in a Firearm course. It is a training day at the shooting range.
You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a 
single space:
Your position is marked with the symbol "A"
Targets marked with symbol "x"
All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number of commands you will receive. The possible 
commands are:
"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if 
the field you want to step on is marked with ".".
"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). 
Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only 
the nearest target. When you have shot a target, the field becomes empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.". 
If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} 
targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Input
5 lines representing the field (symbols, separated by a single space)
N - count of commands
On the following N lines - the commands in the format described above
Output
On the first line, print one of the following:
If all the targets were shot
"Training completed! All {count_targets} targets hit."
Otherwise:
              	       "Training not completed! {count_left_targets} targets left."
Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
'''