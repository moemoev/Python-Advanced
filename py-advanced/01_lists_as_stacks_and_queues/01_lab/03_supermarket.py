from collections import deque

customers = deque()
cmd = input()

while not cmd == 'End':
    if cmd == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(cmd)
    cmd = input()
print(f"{len(customers)} people remaining.")


'''
TASK:
Tom is working at the supermarket, and he needs your help to keep track of his clients. Write a program which reads 
lines of input consisting of a customer's name and adds it to the end of a queue until "End" is received. If in a 
meantime you receive the command "Paid", you should print each customer in the order they are served (from the first to 
the last one) and empty the queue. When you receive "End", you should print the count of the remaining people in the 
queue in the format: "{count} people remaining.".
'''