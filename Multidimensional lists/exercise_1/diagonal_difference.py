# input1 = """3
# 11 2 4
# 4 5 6
# 10 8 -12
# """
# input2 = """4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14
# """
# sys.stdin = StringIO(input2)

n = int(input())
matrix = [[int(el) for el in input().split()] for row in range(n)]

sum_prim_diagonal = 0
sum_secnd_diagonal = 0

for i in range(n):
    sum_prim_diagonal += matrix[i][i]
    #  did the change from the previous task where i did copy tutors way to go on my own, so that makes me go to 11
    sum_secnd_diagonal += matrix[i][n - i - 1]
print(abs(sum_prim_diagonal - sum_secnd_diagonal))


'''
TASK:
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).

On the first line, you will receive an integer N - the size of a square matrix. The next N lines holds the values for 
each column - N numbers separated by a single space. Print the absolute difference between the sums of the primary and 
the secondary diagonal.
'''