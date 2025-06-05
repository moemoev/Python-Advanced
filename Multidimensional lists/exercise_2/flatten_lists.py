import sys
from io import StringIO
import re

input1 = """1 2 3 |4 5 6 |  7  88"""
input2 = """7 | 4  5|1 0| 2 5 |3 0"""
input3 = """1| 4 5 6 7  |  8 -679.067 -1|1 2 345"""

sys.stdin = StringIO(input3)
# pattern = r"-?\d*\.{0,1}\d+"
#
# lists = [el for el in input().split("|")]
#
# matrix = []
# for list in lists:
#     matrix.append(re.findall(pattern, list))
#
# matrix = matrix[::-1]
# for row in range(len(matrix)):
#     print(" ".join(matrix[row]), end=" ")

sets = [el for el in input().split("|")]
subsets = []
for set in sets[::-1]:
    subsets.extend([el.strip() for el in set.split()if not el == ' '])
print(*subsets)

'''
TASK:
Write a program to flatten several lists of numbers received in the following format:
String with numbers or empty strings separated by "|"
Values are separated by spaces (" ", one or several)
Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below
'''