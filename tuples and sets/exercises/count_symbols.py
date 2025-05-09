import sys
from io import StringIO

# input1 = """SoftUni rocks"""
# input2 = """Why do you like Python?"""
# sys.stdin = StringIO(input1)

text = input()
occurrences_by_char = {}

for el in text:
    if el not in occurrences_by_char:
        occurrences_by_char[el] = 0
    occurrences_by_char[el] += 1

for key, val in sorted(occurrences_by_char.items(), key=lambda x: x[0]):
    print(f"{key}: {val} time/s")


'''
TASK:
Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results 
in alphabetical (lexicographical) order.  
'''