def even_odd(*args):
    cmd = args[-1]
    even = []
    odd = []
    for el in args[:-1]:
        if el % 2 == 0:
            even.append(el)
        else:
            odd.append(el)
    if cmd == 'even':
        return even
    else:
        return odd

#note this is a very elegant way of solving via generators plus on top we are using a parity 'bit'
# looks pretty advanced, i have to implement that way of coding! readibility might get lost but looks fancy indeed

# def even_odd(*args):
#     cmd = args[-1]
#     parity = 0 if cmd == 'even' else 1
#     return sum(filter(lambda x: x % 2 == parity, args[:-1])) * (len(args) - 1)



print(even_odd(1, 3, 5, 34, 7, 9, 12, 11, 13, 10, "odd"))


'''
TASK:
Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The 
command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the 
function in the judge system.
'''