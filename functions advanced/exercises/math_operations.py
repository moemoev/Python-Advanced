from collections import deque

operation = deque()


def sort_format_dict(nums_by_op: dict):
    result = ''
    for key, val in sorted(nums_by_op.items(), key=lambda x: (-x[1], x[0])):
        result += f"{key}: {val:.1f}\n"
    return result


def math_operations(*args, **kwargs):
    kwargs_queue = deque(['a', 's', 'd', 'm'])
    for el in args:
        if kwargs_queue[0] == 'a':
            kwargs[kwargs_queue[0]] += el
        elif kwargs_queue[0] == 's':
            kwargs[kwargs_queue[0]] -= el
        elif kwargs_queue[0] == 'm':
            kwargs[kwargs_queue[0]] *= el
        elif kwargs_queue[0] == 'd' and not el == 0:
            kwargs[kwargs_queue[0]] /= el
        kwargs_queue.append(kwargs_queue.popleft())

    return sort_format_dict(kwargs)


print(math_operations(6.0, a=0, s=0, d=5, m=0))


'''
TASK:
Write a function named math_operations that receives a different number of integers as arguments and 4 keyword arguments. 
The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
You need to take each integer argument from the sequence and do mathematical operations as follows:
The first element should be added to the value of the key "a" 
The second element should be subtracted from the value of the key "s" 
The third element should be divisor to the value of the key "d" 
The fourth element should be multiplied by the value of the key "m"
Each result should replace the value of the corresponding key
You must repeat the same steps consecutively until you run out of numbers
Beware: You cannot divide by 0. If the operation could throw an error, you should delete the element from the sequence 
and continue to the next operation.
For more clarifications, see the examples below.
Note: Submit only the function in the judge system
Input
There will be no input. Just parameters passed to your function.
All of the given numbers will be valid integers in the range [-100, 100]
Output
The function should return the final dictionary
'''