import sys
from io import StringIO
from collections import deque

# input1 = """5 6
# SoftUni
# """
# input2 = """1 4
# Python
# """
#
# sys.stdin = StringIO(input1)
rows, cols = [int(el) for el in input().split()]
snake = deque(input())
matrix = []

for row in range(rows):
    matrix.append(deque())
    for col in range(cols):
        if row % 2 == 0:
            matrix[row].append(snake[0])
            snake.append(snake.popleft())
        else:
            matrix[row].appendleft(snake[0])
            snake.append(snake.popleft())
for row in range(rows):
    print("".join(matrix[row]))


'''
TASK:
You are tasked to visualize a snake's zigzag path in a rectangular matrix with size N x M. 
The snake is represented by a string. It starts moving from the top-left corner to the right. When the snake reaches 
the end of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end. 
The first cell is filled with the first symbol of the snake, the second cell is filled with the second symbol, etc. The 
snake's path is long as it takes to fill the matrix completely - if you reach the end of the string representing the snake, 
start again at the first symbol. At the end you should print the snake's path.
Input
The input data consists of exactly two lines:
On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}". 
On the second line you will receive the string representing the snake
Output
You should print the snake's zigzag path of size N x M (rows x columns)
'''

