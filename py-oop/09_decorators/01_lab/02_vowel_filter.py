from functools import wraps

def vowel_filter(function):
    vowels = 'aeiou'
    @wraps(function)
    def wrapper():
        letters = function()
        result = [el for el in letters if el in vowels]
        return result
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
print(get_letters.__name__)