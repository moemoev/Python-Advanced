def age_assignment(*args, **kwargs):
    age_by_name = {arg: kwargs[arg[0]] for arg in args} #  same stuff as stuff below but just naiser usin dict comprehension
    # age_by_name = {}
    # for arg in args:
    #     age_by_name.update({arg: kwargs[arg[0]]})
    result = ''
    for name, age in sorted(age_by_name.items(), key=lambda x: x[0]):
        result += f"{name} is {age} years old.\n"
    return result

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


'''
TASK:
Create a function called age_assignment that receives a different number of names and a different number of key-value 
pairs. The key will be a single letter (the first letter of each name) and the value - a number (age). Find its first 
letter in the key-value pairs for each name and assign the age to the person's name. It the end, return a dictionary 
with all the names and ages as shown in the example. Submit only the function in the judge system.
'''