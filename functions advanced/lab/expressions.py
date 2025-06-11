#note has to be done several times, i did copy it from the lecture without thinking to much about it sicne it is recursion
#note try to do it on your own several times until it becomes a habit


def expressions(numbers, current_result, expression=''):
    if not numbers:
        return [(expression, current_result)]
    result_plus = expressions(
        numbers[1:],
        current_result + numbers[0],
        f'{expression}' '+' f'{numbers[0]}'
    )
    result_minus = expressions(
        numbers[1:],
        current_result - numbers[0],
        f'{expression}' '-' f'{numbers[0]}'
    )
    return result_plus + result_minus


result = expressions([1] * 4, 0)

[print(f'{exp_str}={exp_result}') for (exp_str, exp_result) in result]


'''
TASK:
Write a program that generates all the possible expressions and their results between a given list of numbers (integers) 
using only the + and - operators. Print them on the console, as shown in the example.
'''