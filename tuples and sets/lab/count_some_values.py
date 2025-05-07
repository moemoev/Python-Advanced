import sys
from io import StringIO

#note: not verry awesome way to showcase the use of tuples, can be done vie dict where numbers_in_one_line.txt is key and cound is val then dict.items() returns the tuple....

input1 = """-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3"""
input2 = """2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3"""

sys.stdin = StringIO(input2)

numbers_tt = tuple(float(el) for el in input().split())

already_counted = []

for el in numbers_tt:
    if el not in already_counted:
        print(f"{el} - {numbers_tt.count(el)} times")
        already_counted.append(el)

'''
TASK:
You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in 
the format "{number} - {count} times". The number must be formatted to the first decimal point.
'''