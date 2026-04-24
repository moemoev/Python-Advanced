import sys
from io import StringIO

# input1 = """6
# George
# George
# George
# Peter
# George
# NiceGuy1234"""
# input2 = """10
# Peter
# Maria
# Peter
# George
# Steve
# Maria
# Alex
# Peter
# Steve
# George"""
#
# sys.stdin = StringIO(input1)

number_names = int(input())
set_of_names = set()

for _ in range(number_names):
    set_of_names.add(input())

print("\n".join(set_of_names))


'''
TASK:
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. On 
the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the collection on 
the console (the order does not matter):
'''