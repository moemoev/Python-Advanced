# to test this at full range, delete txt file
try:
    file = open('text1.txt', 'r')
    print(f"File found")
except FileNotFoundError:
    print(f"File not found")

'''
TASK:
You are given a file called text.txt with the following text:

Create program that opens the file. If the file is found, print 'File found'. If the file is not found, print 'File not 
found'.
'''