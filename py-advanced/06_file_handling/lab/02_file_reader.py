# note: in case the numbers are in a single line seperated by spaces
file = open('numbers_in_one_line.txt', 'r')
text = file.readline()
numbers = [int(el) for el in text.split(" ")]
print(f'Numbers in one line sep by " "')
print(sum(numbers))

file = open('numbers_in_multiple_lines.txt', 'r')
numbers = [int(line) for line in file]
print(f"one number each line")
print(sum(numbers))

# TODO: keep in mind that if u use big data sets the listcomprehension might be ba dpractice since everything will be read into memor at once, a for loop would help


'''
TASK:
You are given a file called numbers.txt with the following content:

Create a program that reads the numbers from the file. Print on the console the sum of those numbers.
'''