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
You are driving a truck on a circle road with N petrol pumps on it. The petrol pumps are numbered 0 to (N−1) (both inclusive). 
For each petrol pump you will receive two pieces of information (separated by a single space): 
the amount of petrol that petrol pump will give
the distance from that petrol pump to the next petrol pump (kilometers)
Initially, you have a tank of infinite capacity carrying no petrol. The truck can start the tour at any of the petrol 
pumps and it will move one kilometer for each liter of the petrol. Calculate the first point from where the truck will 
be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. 
Input
On the first line you will receive the number of petrol pumps - N
On the next N-lines you will receive the amount of petrol that petrol pump will give and the distance between that petrol 
pump and the next petrol pump, separated by single space
Output
An integer which will be the smallest index of a petrol pump from which you can start the tour
Constraints
'''