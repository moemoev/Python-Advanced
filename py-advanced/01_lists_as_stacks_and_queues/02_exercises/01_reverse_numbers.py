import sys
from io import StringIO


# input1 = """1 2 3 4 5"""
# input2 = """1"""
#
# sys.stdin = StringIO(input2)

numbers_stack = [int(el) for el in input().split()]


while numbers_stack:
    print(numbers_stack.pop(), end=" ")


'''
TASK:
Write a program which reads from the console a string with N integers, separated by a single space, and reverses them 
using a stack. Print the reversed integers on one line, separated by a single space.
'''