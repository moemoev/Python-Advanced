import sys
from collections import deque
from io import StringIO

# input1 = """20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
# """
# input2 = """-10, -2, -30, 10
# -5
# """
#
# input3 = """2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
# """
#
# sys.stdin = StringIO(input1)

# choco as stack, milk as queue
chocolates = [int(el) for el in input().split(", ")]
milks = deque(int(el) for el in input().split(", "))

count_milkshakes = 0
expected_milkshakes = 5  # hardcoded, can be dynamic
milkshake_goal_reached = False


def values_greater_zero():
    if not 0 < milks[0] or not 0 < chocolates[-1]:
        if not 0 < milks[0]:
            milks.popleft()
        if not 0 < chocolates[-1]:
            chocolates.pop()
        return False
    return True


while chocolates and milks:
    if not values_greater_zero():
        continue
    if milks[0] == chocolates[-1]:
        chocolates.pop()
        milks.popleft()
        count_milkshakes += 1
    else:
        chocolates[-1] -= 5
        milks.append(milks.popleft())
    if count_milkshakes == 5:
        milkshake_goal_reached = True
        break

if milkshake_goal_reached:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print("Chocolate:", ", ".join(str(el) for el in chocolates))
else:
    print("Chocolate: empty")
if milks:
    print("Milk:", ", ".join(str(el) for el in milks))
else:
    print("Milk: empty")
