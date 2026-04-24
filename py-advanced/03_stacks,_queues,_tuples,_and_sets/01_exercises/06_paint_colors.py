import sys
from io import StringIO
from collections import deque

# input1 = """d yel blu e low redd"""
# input2 = """r ue nge ora bl ed"""
# input3 = """re ple blu pop e pur d"""
# sys.stdin = StringIO(input1)


primary_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}

formed_colors = []
substrings = deque(input().split())

calls = 0


def substr_form_color():
    potential_color = substrings[0] + substrings[-1]
    if potential_color in primary_colors or potential_color in secondary_colors:
        formed_colors.append(substrings.popleft() + substrings.pop())
        return True
    potential_color = substrings[-1] + substrings[0]
    if potential_color in primary_colors or potential_color in secondary_colors:
        formed_colors.append(substrings.pop() + substrings.popleft())
        return True
    return False


def check_single_substr(substr: str):
    if substr in primary_colors or substr in secondary_colors:
        formed_colors.append(substr)
    return True


def substr_into_middle(len_substr: int):
    sub_1 = substrings.popleft()
    sub_2 = substrings.pop()
    if 1 < len(sub_1):
        substrings.insert((len_substr - 2) // 2, sub_1[:len(sub_1) - 1])
    if 1 < len(sub_2):
        substrings.insert((len_substr - 2) // 2, sub_2[:len(sub_2) - 1])
    return


def check_sec_colors():
    for color in formed_colors:
        if color in secondary_colors:
            sec_color_meets_requirements(color)
    return


def sec_color_meets_requirements(sec_col: str):
    if sec_col == 'orange':
        if 'red' not in formed_colors or 'yellow' not in formed_colors:
            formed_colors.remove('orange')
    elif sec_col == 'purple':
        if 'red' not in formed_colors or 'blue' not in formed_colors:
            formed_colors.remove('purple')
    elif sec_col == 'green':
        if 'yellow' not in formed_colors or 'blue' not in formed_colors:
            formed_colors.remove('green')
    return


while substrings:
    calls = 0
    if len(substrings) == 1:
        check_single_substr(substrings.popleft())
        continue
    if substr_form_color():
        continue
    number_substr = len(substrings)
    # if number_substr % 2 == 0:  # even
    substr_into_middle(number_substr)

check_sec_colors()
print(formed_colors)
