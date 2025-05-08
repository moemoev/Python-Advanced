import sys
from io import StringIO

input0 = """8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey
"""
input1 = """7
Lyle
Bruce
Alice
Easton
Shawn
Alice
Shawn
"""
input2 = """6
Adam
Adam
Adam
Adam
Adam
Adam
"""

sys.stdin = StringIO(input2)

number = int(input())

# names = set()
# for _ in range(number):
#     names.add(input())
# note: or ...
names = {input() for _ in range(number)}

for el in names:
    print(el)

'''
TASK:
Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
'''