import sys
from io import StringIO


input1 = """1 2 -3 -4 65 -98 12 57 -84"""
# input2 = """1 2 3"""
sys.stdin = StringIO(input1)
def seperate_numbers(num: list):
    #     positive = []
    #     negative = []
    #     for el in num:
    #         if el < 0:
    #             negative.append(el)
    #         else:
    #             positive.append(el)
    negative = filter(lambda x: x < 0, num)
    positive = filter(lambda x: x > 0, num)
    return sum(negative), sum(positive)


numbers = [int(el) for el in input().split()]
neg, pos = seperate_numbers(numbers)

print(f"{neg}")
print(f"{pos}")
if abs(neg) < pos:
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")


'''
TASK:
You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the 
positive. Find the total sum of the negatives and positives, and print the following:
On the first line, print the sum of the negatives
On the second line, print the sum of the positives
On the third line:
If the absolute negative number is larger than the positive number:
	"The negatives are stronger than the positives"
If the positive number is larger than the absolute negative number:
	"The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.
'''