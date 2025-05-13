algebraic_expression = input()
stack_of_indices = []
for i in range(len(algebraic_expression)):
    if algebraic_expression[i] == '(':
        stack_of_indices.append(i)
    elif algebraic_expression[i] == ')':
        print(algebraic_expression[stack_of_indices.pop():i + 1])

'''
TASK:
You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
Print the result back on the console.
'''