'''
This task is way to hard unless you are very familiar with recursion, it was taken out of the lecture material afterwards.
focusing on the mere realization of recursion is just overkill but if u have some experience it is an awesome example.
unlike the lab wanted i did not realize count of the permutations but its basically len(values)!
https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/ example of permutation recursion tree
very good once at this lvl of algorythms
'''


def perm(index: int, values: list):
    if index == len(values):
        print("".join(values))
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        perm(index + 1, values)
        values[i], values[index] = values[index], values[i]


perm(0, list("abcd"))


'''
TASK:
Write a program that reads a single string and prints all possible combinations of the characters in that string. Submit 
your solution in the judge system.
'''
