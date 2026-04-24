import sys
from io import StringIO

# input1 = """4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5"""
# input2 = """2 2
# 1
# 3
# 1
# 5"""
#
# sys.stdin = StringIO(input2)

n_elements, m_elements = [int(el) for el in input().split()]
set_n = set()
set_m = set()

for i in range(n_elements):
    set_n.add(input())
for i in range(m_elements):
    set_m.add(input())

for el in set_n & set_m:
    print(el)


'''
TASK:
Write a program which prints a set of elements. On the first line, you will receive two numbers - n and m, separated by 
a single space - they represent the lengths of two separate sets. On the next n + m lines you will receive n numbers, 
which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that 
appear in both and print them on separate lines (the order does not matter).
'''