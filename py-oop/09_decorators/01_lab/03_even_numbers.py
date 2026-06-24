from functools import wraps


def even_numbers(function):
    @wraps(function)
    def wrapper(numbers):
        nums= function(numbers)
        even_nums = [el for el in nums if el % 2 == 0]
        return even_nums

    return wrapper


@even_numbers
def get_numbers(numbers):

    return numbers



print(get_numbers([1, 2, 3, 4, 5]))
