'''
again very rough for that lvl of knowledge but still a nais task

'''


def generate_combinations(values, index, count, comb):
    if len(comb) == count:
        print(comb)
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        generate_combinations(values, i + 1, count, comb)
        comb.pop()


generate_combinations(['p', 'g', 'a'], 0, 2, [])


'''
TASK:
Write a program that receives names on the first line (separated by comma and space ", ") and a number of chairs on the 
second line (an integer). The chairs will always be less than the people. Find all the ways to fit those people on the 
chairs. Print each combination on a separate line.
Note: In the example below, "Peter, George" is the same as "George, Peter", so we only print the first combination
'''