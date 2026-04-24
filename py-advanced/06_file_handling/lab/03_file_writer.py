text = f"I just create my first file Fucker!"
file_path = 'my_first_file.txt'
mode = 'w'

with open(file_path, mode) as file:
    file.write(text)


'''
TASK:
Create a program that creates a file called my_first_file.txt. In that file write a single line with the content: 'I just 
created my first file!'
'''