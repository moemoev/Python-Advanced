def fill_the_box(height, length, width, *args):
    volume = height * length * width
    i = 0
    sum_cubes = 0
    while not args[i] == 'Finish':
        if sum_cubes + args[i] > volume:
            return f"No more free space! You have {sum(args[i:len(args) - 1]) - (volume - sum_cubes)} more cubes."
        sum_cubes += args[i]
        i += 1
    return f"There is free space in the box. You could put {volume - sum_cubes} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

'''
TASK:
Write a function called fill_the_box that receives a different number of arguments representing:
the height of a box
the length of a box
the width of a box
n-times a different number of cubes with exact size 1 x 1 x 1
a string "Finish"
Your task is to fill the box with the given cubes until the current argument equals "Finish".
Note: Submit only the function in the judge system
Input
'''