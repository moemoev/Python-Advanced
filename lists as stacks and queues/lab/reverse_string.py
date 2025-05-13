text = input()
stack = []
for el in text:
    stack.append(el)

while stack:
    print(stack.pop(), end="")


'''
TASK:
Write program that:
Reads an input string
Reverses it using a stack
Prints the result back on the console
'''