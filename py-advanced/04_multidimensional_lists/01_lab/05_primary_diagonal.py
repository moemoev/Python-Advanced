import sys
from io import StringIO

# input1 = """3
# 11 2 4
# 4 5 6
# 10 8 -12
# """
# input2 = """	3
# 1 2 3
# 4 5 6
# 7 8 9
# """
#
# sys.stdin = StringIO(input2)

n = int(input())

matrix = []
for i in range(n):
    matrix.append([int(el) for el in input().split()])


sum_diagonal = 0
for i in range(n):
    sum_diagonal += matrix[i][i]

print(sum_diagonal)


'''
TASK:
Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). 
On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the values for 
each column - N numbers, separated by a single space. 
'''