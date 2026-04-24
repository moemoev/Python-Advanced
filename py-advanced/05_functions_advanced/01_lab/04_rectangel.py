def rectangle(length, width):
    if not type(length) == int or not type(width) == int:
        return "Enter valid values!"
    return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"


def area(length: int, width: int):
    return length * width


def perimeter(length: int, width: int):
    return 2 * (width + length)


print(rectangle('2', 10))


'''
TASK:
Create a function called rectangle(). It must have two parameters - length and width. 
First, you need to check if the given arguments are integers:
If one/ both of them is/ are NOT integer/s, return the string "Enter valid values!"
Create two inner functions:
area() - returns the area of the rectangle with the given length and width
perimeter() - returns the perimeter of the rectangle with the given length and width
In the end, the rectangle function should return a string containing the area and the perimeter of a rectangle in the 
following format:
"Rectangle area: {ract_area}
Rectangle perimeter: {rect_perim}"
'''