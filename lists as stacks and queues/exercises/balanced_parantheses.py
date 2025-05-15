import sys
from collections import deque
from io import StringIO

# input1 = """3
# 1 5
# 10 3
# 3 4
# """
# input2 = """5
# 22 5
# 14 10
# 52 7
# 21 12
# 36 9
# """
#
# sys.stdin = StringIO(input2)
stations = int(input())
gas_stations = deque()
distances = deque()

def check_circletrip(gas: deque, dist: deque, count_stations: int):
    sum_petrol = 0
    sum_distance = 0
    for _ in range(count_stations):
        sum_petrol += gas.popleft()
        sum_distance += dist.popleft()
        if sum_petrol < sum_distance:
            return False
    return True

# initializing the two queues
for _ in range(stations):
    petrol, distance = [int(el) for el in input().split()]
    gas_stations.append(petrol)
    distances.append(distance)

starting_index = 0
starting_station_found = False

while True:

    starting_station_found = check_circletrip(gas_stations.copy(), distances.copy(), stations)
    if starting_station_found:
        break
    starting_index += 1
    gas_stations.append(gas_stations.popleft())
    distances.append(distances.popleft())
print(starting_index)


'''
TASK:
You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced. A 
sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs after 
the former. There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].
{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
Input
On a single line you will receive a sequence of parentheses.
Output 
For each test case, print on a new line "YES" if the parentheses are balanced. 
Otherwise, print "NO". Do not print the quotes.
'''