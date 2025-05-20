import sys
from io import StringIO

# input1 = """1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset
# """
# input2 = """5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
# """
#
# sys.stdin = StringIO(input1)

first_set = set(int(el) for el in input().split())
second_set = set(int(el) for el in input().split())

n = int(input())

for _ in range(n):
    cmd, subset, *numbers = [el for el in input().split()]
    numbers = set(int(el) for el in numbers)
    if cmd == 'Add' and subset == 'First':
        first_set.update(set(numbers))
    elif cmd == 'Add' and subset == 'Second':
        second_set.update(set(numbers))
    elif cmd == 'Remove'and subset == 'First':
        first_set.difference_update(set(numbers))
    elif cmd == 'Remove'and subset == 'Second':
        second_set.difference_update(set(numbers))
    else:
        print(first_set.issubset(second_set) or first_set.issuperset(second_set))


print(", ".join(str(el) for el in sorted(first_set)))
print(", ".join(str(el) for el in sorted(second_set)))