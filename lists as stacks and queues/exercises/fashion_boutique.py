import sys
from io import StringIO
from time import time

# input1 = """5 4 8 6 3 8 7 7 9
# 16
# """
# input2 = """1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
# 20
# """
# sys.stdin = StringIO(input2)

pile_of_clothes = [int(el) for el in input().split()]
rack_capacity = int(input())
count_racks = 0
current_rack = 0

while pile_of_clothes:
    # peek into the pile_of_clothes then pop it, could pop it from stack into a key and then process accordingly
    # looks pretty unhandy with the peek usage for someone else, but as of now i like it cuz it makes me look pro...
    if rack_capacity >= current_rack + pile_of_clothes[-1]:
        current_rack += pile_of_clothes.pop()
    else:
        count_racks += 1
        current_rack = 0

if current_rack:
    print(count_racks + 1)
else:
    print(count_racks)


'''
TASK:
You own a fashion boutique, and you receive a delivery of a huge box of clothes, represented as a sequence of integers. 
On the next line, you will be given an integer representing the capacity for one rack in your store.  
You must arrange the clothes in the store, and you use the racks to hang up every piece of clothing. You start from the 
last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for the purpose. Each piece of 
clothing has its value (an integer). You must sum their values, while you take them out of the box:
If the sum becomes equal to the capacity of the current rack you must take a new one for the next clothes (if there are 
any left in the box). 
If the sum becomes greater than the capacity, do not hang the piece of clothing to the current rack. Take a new rack and 
then hang it up.
In the end, print how many racks you have used to hang up the clothes.
Input
On the first line you will be given a sequence of integers, representing the clothes in the box, separated by a single space.
On the second line, you will be given an integer, representing the capacity of a rack.
Output
Print the number of racks, needed to hang up the clothes from the box.
'''