def func_executor(*args):
    result = ''
    for func, param in args:
        result += func.__name__ + " - " + str(func(*param)) + '\n'
    return result


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

'''
TASK:
Create a function called func_executor() that can receive a different number of tuples, each of which will have exactly 
2 elements: first will be a function, and the second will be a tuple of the arguments that need to be passed to that 
function. Create a list that will contain all the results of the executed functions with their corresponding arguments 
and return it after executing all functions. For more clarification, see the examples below. Submit only your function 
in the judge system.
'''