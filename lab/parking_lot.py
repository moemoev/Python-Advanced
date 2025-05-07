import sys
from io import StringIO

# input1 = """10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU
# """
# input2 = """4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA"""
#
# sys.stdin = StringIO(input2)

number_actions = int(input())

parking_lot = set()

for _ in range(number_actions):
    direction, car_id = input().split(", ")
    if direction == 'IN':
        parking_lot.add(car_id)
    elif direction == 'OUT':
        parking_lot.discard(car_id)

if parking_lot:
    [print(el) for el in parking_lot]
else:
    print(f"Parking Lot is Empty")


'''
TASK:
Write a program that:
Records a car number for every car that enters the parking lot
Removes a car number when the car leaves the parking lot
On the first line, you will receive the number of commands - N. On the following N lines, you will receive the direction 
and car's number in the format: "{direction}, {car_number}". The direction could only be "IN" or "OUT". Print the car
numbers which are still in the parking lot. Keep in mind that all car numbers must be unique. If the parking lot is empty, 
print "Parking Lot is Empty".
Note: The order in which we print the result does not matter.
'''