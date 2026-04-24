import sys
from collections import deque
from io import StringIO
from operator import truediv

# input1 = """10 -5 20 15 -30 10
# 40 60 10 4 10 0
# """
# input2 = """30 5 15 60 0 30
# -15 10 5 -15 25
# """
# input3 = """30 10
# 15 10 5 0 10
# """
#
# sys.stdin = StringIO(input3)

materials = [int(el) for el in input().split()]
magics = deque(int(el) for el in input().split())

presents_by_magic = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

# presents that will be manufactured during prog. and to achieve presents
manufactured_presents = {}
present_pair_1 = {'Doll', 'Wooden train'}
present_pair_2 = {'Teddy bear', 'Bicycle'}
successful_manufacturing = False


def add_present_to_manuf_presnts(m_level: int):
    # check if string of craftable presents exists within manufuctered, if not creat, then increase count
    if presents_by_magic[magic_level] not in manufactured_presents:
        manufactured_presents[presents_by_magic[magic_level]] = 0
    manufactured_presents[presents_by_magic[m_level]] += 1
    return


def remove_zero_vals():
    if materials[-1] == 0:
        materials.pop()
    if magics[0] == 0:
        magics.popleft()
    return


def process_status():
    if present_pair_1.issubset(manufactured_presents):
        return True
    if present_pair_2.issubset(manufactured_presents):
        return True
    return False


while materials and magics:
    # compute magic_lvl-> check corresponding crftble item, remove val from crafting process,-> add item accordingly
    magic_level = materials[-1] * magics[0]
    if magic_level in presents_by_magic:
        materials.pop()
        magics.popleft()
        add_present_to_manuf_presnts(magic_level)
    elif magic_level < 0:
        magic_level = materials.pop() + magics.popleft()
        materials.append(magic_level)
    elif magic_level == 0:
        remove_zero_vals()
    else:
        magics.popleft()
        materials[-1] += 15

if process_status():
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print("Materials left:", ", ".join(str(el) for el in materials[::-1]))
if magics:
    print("Magic left:", ", ".join(str(el) for el in magics))
for present, quantity in sorted(manufactured_presents.items(), key=lambda x: x[0]):
    print(f"{present}: {quantity}")
