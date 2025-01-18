# a program that calculates the area and perimeter of a rectangle
length = float(input("Enter the length of rectangle:"))
width = float(input("Enter the width of rectangle:"))
area = length*width
perimeter = 2*(length+width)
print(f"The area of rectangle is: {area}")
print(f"The perimeter of rectangle is:{perimeter}")