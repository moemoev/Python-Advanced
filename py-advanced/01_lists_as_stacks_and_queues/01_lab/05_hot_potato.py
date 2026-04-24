from collections import deque
import sys
from io import StringIO

# input1 = """Tracy Emily Daniel
# 2
# """
# input2 = """George Peter Michael William Thomas
# 10
# """
#
# input3 = """George Peter Michael William Thomas
# 1
# """
# sys.stdin = StringIO(input3)

children = deque()
for el in input().split():
    children.append(el)

n_toss = int(input())
toss_count = 0

while 1 < len(children):
    toss_count += 1
    if not toss_count % n_toss == 0:
        children.append(children.popleft())
    else:
        print(f"Removed {children.popleft()}")
        # toss_count = 0
print(f"Last is {children.popleft()}")


'''
TASK:
Hot Potato is a game in which children form a circle and start tossing a hot potato. The counting starts with the first 
kid. Every nth toss the child who is holding the potato leaves the game. When a kid leaves the game, it passes the potato 
to the next kid. This continues until there is only one kid left.
Create a program that simulates the game of Hot Potato. On the first line you will receive names of kids, separated by 
a single space. On the second line you will receive the nth toss (integer) in which a child leaves the game.
Print every kid which is removed from the circle in the format "Removed {kid}". In the end, print the only kid left in 
the format "Last is {kid}".
'''