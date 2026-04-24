# note: opening the file "main.py" which is within the same directory
file = open('main.py', 'r')
print(file.readlines())

# note: opening a file from a nested directory(lower lvl) using relative path
file = open('test_file_handling/test_reading_files.py', 'r')
print(file.readlines())

# note: opening a file from wherever using the absulute path, which is easy in pycharm since we can copy it, otherwise use the console
file = open(r"C:\Users\dimod\PycharmProjects\MyFirstProject\Python_Advanced_Softuni\pythonProject1\test_file_reading_from_outer_scope.py", 'r')
print(file.readlines())