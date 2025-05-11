import sys
from io import StringIO

# input1 = """4
# Ce O
# Mo O Ce
# Ee
# Mo"""
# input2 = """3
# Ge Ch O Ne
# Nb Mo Tc
# O Ne"""
#
# sys.stdin = StringIO(input2)

number_lines = int(input())
unique_chemicals = set()

for _ in range(number_lines):
    new_chemicals = set(el for el in input().split())
    # used the set operator instead of goin through each input and set.add() single elements
    unique_chemicals = unique_chemicals|new_chemicals
print("\n".join(unique_chemicals))


'''
TASK:
Write a program that keeps all the unique chemical elements. On the first line you will be given a number n - the count 
of input lines that you are going to receive. On the next n lines, you will be receiving chemical compounds, separated 
by a single space. Your task is to print all the unique ones on separate lines (the order does not matter):
'''