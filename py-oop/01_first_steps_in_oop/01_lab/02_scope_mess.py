x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x     # nonlocal is ised in nested fctns and sets the var in the parent-fctn to the val
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)


'''
x = "global"

def outer():
    x = "local"    
    
    def inner():
        x = "nonlocal"
        print("inner:", x)
    
    def change_global():
        x = "global: changed!"    
    
    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)

'''

'''
Task:
Fix the code above so it returns the expected output. Submit the fixed code in the judge system.
Current Output

global
outer: local
inner: nonlocal
outer: local
global

Expected Output 

global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!

'''