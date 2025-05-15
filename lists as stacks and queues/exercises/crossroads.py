import sys
from io import StringIO
from collections import deque

# input1 = """10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END"""
# input2 = """9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END"""
#
# sys.stdin = StringIO(input1)

green_time = int(input())
window_time = int(input())
cars = deque()
total_cars = []
crash_happened = False


def green_crossing(green: int, window: int):
    crasch = False
    length_car = len(cars[0])
    if length_car <= green:
        green -= length_car
        total_cars.append(cars.popleft())
        return green, crasch
    if length_car - green <= window:
        total_cars.append(cars.popleft())
    else:
        crash(green + window, cars.popleft())
        crasch = True
    green = 0
    return green, crasch


def crash(time: int, car: str):
    print(f"A crash happened!")
    print(f"{car} was hit at {car[time]}.")


cmd = input()
while not cmd == 'END':
    green_phase = green_time
    if not cmd == 'green':
        cars.append(cmd)
    if cmd == 'green':
        while green_phase and cars:
            green_phase, crash_happened = green_crossing(green_phase, window_time)
    if crash_happened:
        break
    cmd = input()
if not crash_happened:
    print(f"Everyone is safe.")
    print(f"{len(total_cars)} total cars passed the crossroads.")

'''
TASK:
The super-spy action hero Sam has finally found some time to go on a holiday. He is taking his wife somewhere nice and 
they're going to have a really good time, but first, they have to get there. Even on his holiday trip, Sam is still going 
to run into some problems and the first one is getting to the airport. Right now, he is stuck in a traffic jam at a 
crossroads where a lot of accidents happen.
Your job is to keep track of the traffic at the crossroads and report whether a crash happened or everyone passed the 
crossroads safely.
Sam is on a single lane of cars which queue up until the light goes green. When it does, they start passing one by one 
on a flashing green light and during the free window before the intersecting road's light goes green. For each second 
only one part of a car (a single character) passes the crossroad. If a car is still in the middle of the crossroads when 
the free window ends, it will get hit at the first character that is still in the crossroads.
Input
On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
On the following lines, until you receive the "END" command, you will receive one of two things:
A car – a string containing the model of the car, or
The command "green" which indicates the start of a green light cycle
A green light cycle goes as follows:
During the green light cars will enter and exit the crossroads one by one
During the free window cars will only exit the crossroads
Output
If a crash happens, end the program and print:
"A crash happened!"
"{car} was hit at {character_hit}."
If everything goes smoothly and you receive an "END" command, print:
"Everyone is safe."
"{total_cars_passed} total cars passed the crossroads."
'''