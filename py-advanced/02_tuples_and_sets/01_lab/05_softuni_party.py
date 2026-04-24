import sys
from io import StringIO

input1 = """5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END
"""
input2 = """6
m8rfQBvl
fc1oZCE0
UgffRkOn
7ugX7bm0
9CQBGUeJ
2FQZT3uC
2FQZT3uC
9CQBGUeJ
fc1oZCE0
END
"""

sys.stdin = StringIO(input2)

number = int(input())
regular_guest_list = []
vip_guest_list = []
guests_at_party = set()

for _ in range(number):
    guest = input()
    if guest[0].isdigit():
        vip_guest_list.append(guest)
    else:
        regular_guest_list.append(guest)

#note: this is a very unhandy way, if u just remove the guests(which did come)
# from the guest list, the remaining guests on the list are the one we are looking for(set difference "-" set works too)
guest = input()
while not guest == 'END':
    if guest in vip_guest_list or guest in regular_guest_list:
        guests_at_party.add(guest)
    if guest in vip_guest_list:
        vip_guest_list.remove(guest)
    else:
        regular_guest_list.remove(guest)
    guest = input()

print(f"{number - len(guests_at_party)}")
for el in sorted(vip_guest_list):
    print(el)
for el in sorted(regular_guest_list):
    print(el)


'''
TASK:
There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP. When a guest 
comes, check if they exist in any of the two reservation lists.
On the first line, you will receive the number of guests – N. On the following N lines, you will be receiving their 
reservation codes. All reservation codes are 8 characters long, and all VIP numbers will start with a digit. Keep in 
mind that all reservation numbers must be unique.
After that, you will be receiving guests who came to the party until you read the "END" command.
In the end, print the number of the guests who did not come to the party and their reservation numbers. The VIP guests 
must be first. Both the VIP and the Regular guests must be sorted in ascending order.
'''