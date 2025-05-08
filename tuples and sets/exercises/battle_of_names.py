import sys
from io import StringIO

input1 = """4
Pesho
Stefan
Stamat
Gosho"""
input2 = """6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan"""
sys.stdin = StringIO(input1)

number_lines = int(input())

odd_set = set()
even_set = set()

for n in range(1, number_lines + 1):
    value_string = 0
    for el in input():
        value_string += ord(el)
    value_string //= n
    if not value_string % 2 == 0:
        odd_set.add(value_string)
    else:
        even_set.add(value_string)

if sum(even_set) < sum(odd_set):
    print(", ".join(str(el) for el in (odd_set - even_set)))
elif sum(even_set) > sum(odd_set):
    print(", ".join(str(el) for el in (odd_set ^ even_set)))
else:
    print(", ".join(str(el) for el in (odd_set | even_set)))


'''
TASK:
You will receive a number N. On the next N lines, you will be receiving names. You must sum the ascii values of each 
letter in the name and integer divide it to the number of the current row (starting from 1). Save the result to a set of 
either odd or even numbers, depending on if the devised number is an odd or even. After that, sum the values of each set.
If the sums of the two sets are equal, print the union of the values, separated by ", ". 
If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric different values, separated 
by ", ".
NOTE: On every operation, the starting set should be the odd set
'''