# Expalin the diff Between = operator & == operator in python
# = is a assignment operators, for assigning a value to a variable
# == is a relationship between two operands
# ex x = 2 _> 2 is assign to the variable x, 4==10 checks whether the relation is equal or not

# what does the ** operator do in python and how is it used?
# ** is a exponentiation operator, it is used to raise the first operand to power of second
x = 3
y = 2
print(x**y)


# what does the ^ operator do in python and what contex is it commonly used?
# It is Bitwise XOR operator
# it compares each bit of two numbers

x = 3
y = 5
print(x^y)

Task #1
Difference between = and == Operators in Python
= Operator: This is the assignment operator. It is used to assign a value to a variable. For example, x = 5 assigns the value 5 to the variable x.

== Operator: This is the equality operator. It is used to compare two values to see if they are equal. For example, x == 5 checks if the value of x is equal to 5.

The ** Operator in Python
The ** operator is the exponentiation operator. It is used to raise a number to the power of another number. For example, 2 ** 3 calculates (2) raised to the power of (3), which equals (8).
The ^ Operator in Python
The ^ operator is the bitwise XOR (exclusive OR) operator. It is used to compare each bit of two numbers and returns a new number whose bits are set to 1 where the corresponding bits of either but not both operands are 1. For example, 5 ^ 3 results in 6 because the binary representation of 5 is 101 and 3 is 011, and the XOR operation results in 110 which is 6 in decimal.
Task #2
Program to Calculate the Area of a Circle
def calculate_circle_area(radius):

    pi = 3.14

    area = pi * (radius ** 2)

    return area



# Example usage

radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)

print(f"The area of the circle with radius {radius} is {area}")
Program to Compare Two Numbers
def compare_numbers(num1, num2):

    if num1 > num2:

        return "The first number is greater than the second number."

    elif num1 < num2:

        return "The first number is less than the second number."

    else:

        return "The first number is equal to the second number."



# Example usage

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

result = compare_numbers(num1, num2)

print(result)
Program to Calculate the Square and Cube of a Number
def calculate_square_and_cube(number):

    square = number ** 2

    cube = number ** 3

    return square, cube



# Example usage

number = float(input("Enter a number: "))

square, cube = calculate_square_and_cube(number)

print(f"The square of {number} is {square}")

print(f"The cube of {number} is {cube}")