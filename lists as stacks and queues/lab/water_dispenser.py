from collections import deque

water = int(input())

queue = deque()
cmd = input()
while not cmd == 'Start':
    queue.append(cmd)
    cmd = input()

cmd = input()
while not cmd == 'End':
    cmd = [el for el in cmd.split()]
    if 'refill' in cmd:
        water += int(cmd[1])
    elif int(cmd[0]) <= water:
        print(f"{queue.popleft()} got water")
        water -= int(cmd[0])
    else:
        print(f"{queue.popleft()} must wait")
    cmd = input()
print(f"{water} liters left")


'''
TASK:
Write a program which keeps track of people who are getting water from a dispenser and the amount of water left at the 
end. 
On the first line you will receive the starting quantity of water (integer) in a dispenser. Then, on the next few lines 
you will be given the names of some people who want to get water (each on separate line) until you receive the command 
"Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the 
dispenser for that person.
If there is enough water, print "{person_name} got water" and remove him/her from the queue.
Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
"refill {liters}" - add the given litters in the dispenser.
At the end print how many litters of water have left in the format: "{left_liters} liters left".
'''