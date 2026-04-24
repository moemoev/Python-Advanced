import sys
from io import StringIO

# input1 = """3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10"""
# input2 = """5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11"""
#
# sys.stdin = StringIO(input2)

number_lines = int(input())
intersections = []
intersection1 = set()
intersection2 = set()

for _ in range(number_lines):
    indexes_inters1, indexes_inters2 = [el for el in input().split("-")]
    start_inter1, end_inter1 = [int(el) for el in indexes_inters1.split(",")]
    start_inter2, end_inter2 = [int(el) for el in indexes_inters2.split(",")]
    intersection1 = set(range(start_inter1, end_inter1 + 1))
    intersection2 = set(range(start_inter2, end_inter2 + 1))
    intersection1_and_2_union = intersection1 & intersection2
    intersections.append((intersection1_and_2_union, len(intersection1_and_2_union)))
max_intersection, length_max_intersection = max(intersections, key=lambda x: x[1])
print(f"Longest intersection is {list(max_intersection)} with length {length_max_intersection}")


'''
TASK:
Write a program which finds the longest intersection. You will be given a number N. On each of the next N lines you will 
be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the 
intersection of these two ranges. The start and end numbers in the ranges are inclusive. 
Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its 
length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.
'''