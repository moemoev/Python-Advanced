def concatenate(*args, **kwargs):
    text = "".join(args)
    for key, val in kwargs.items():
        if key in text:
            text = text.replace(key, val)
    return text


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


'''
TASK:
Write a function called concatenate() that receives some strings, concatenates them, and returns the result.
'''