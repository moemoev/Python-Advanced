import sys
from io import StringIO
from collections import deque

# input1 = """ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End"""
# input2 = """ROB-8
# 7:59:59
# detail
# glass
# wood
# sock
# End"""
#
# input3 = """ROB-8
# 23:59:58
# detail
# glass
# wood
# sock
# End"""
#
# sys.stdin = StringIO(input2)

jobtime_by_robot = {}
active_time_by_robot = {}
for el in input().split(";"):
    robot, jobtime = el.split("-")
    jobtime_by_robot[robot] = int(jobtime)
    active_time_by_robot[robot] = -1

hh, mm, ss = [int(el) for el in input().split(":")]
time_in_s = hh * 3600 + mm * 60 + ss
max_time = 23 * 3600 + 59 * 60 + 60

materials = deque()
cmd = input()
while not cmd == 'End':
    materials.append(cmd)
    cmd = input()


# increase time by 1 sec. if time = 23:59:59 set time to 0
def adjust_time(time: int):
    time += 1
    if time == max_time:
        time = 0
    return time


def print_time(time: int):
    hh = str(time // 3600)
    mm = str((time // 60) % 60)
    ss = str(time % 60)
    return hh, mm, ss


while materials:
    job_taken = False
    time_in_s = adjust_time(time_in_s)
    for robot, scheduled_time in active_time_by_robot.items():
        if scheduled_time <= time_in_s and not job_taken:
            hh, mm, ss = print_time(time_in_s)
            print(f"{robot} - {materials[0]} [{hh.zfill(2)}:{mm.zfill(2)}:{ss.zfill(2)}]")
            materials.popleft()
            active_time_by_robot[robot] = (time_in_s + jobtime_by_robot[robot]) % max_time
            job_taken = True
    if job_taken:
        continue
    materials.append(materials.popleft())

'''
TASK:
omewhere in the future, there is a robotics factory. The current project is assembly line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free 
it should take a product for processing and log his name, product and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first 
product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it, 
it should be queued at the end of the line again.
The robots are standing on the line in the order of their appearance.
Input
On the first line, you will receive the names of the robots and their processing times in the format "robotName-processTime;
robotName-processTime;robotName-processTime..."
On the second line, you will get the starting time in format "hh:mm:ss"
Next, until the "End" command, you will get a product on each line.
Output 
Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
'''
