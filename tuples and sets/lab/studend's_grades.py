import sys
from io import StringIO

# input1 = """7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
# """
# input2 = """4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66
# """
# input3 = """5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30
# """
#
# sys.stdin = StringIO(input1)

number_students = int(input())
grades_by_students = {}

for _ in range(number_students):
    student, grade = input().split()
    if student not in grades_by_students:
        grades_by_students[student] = []
    grades_by_students[student].append(float(grade))

for student, grades in grades_by_students.items():
    print(f"{student} -> {' '.join(str(f'{el:.2f}') for el in grades)} (avg: {sum(grades)/len(grades):.2f})")


'''
TASK:
Write a program that reads students' names and their grades and adds them to the student record.
On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a 
student's name and their grade.
For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in 
the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter.
'''