# Python script that calculate the square and cube of the given number
number = float(input("Enter your number :"))
square = number ** 2
cube = number ** 3
print("square of", number, "is:", square)
print("cube of", number, "is", cube,"\n")

# Create a program that takes two numbers as input & prints whether the first number is greater than, lesser

number1 = (int(input("Enter the 1st number :")))
number2 = (int(input("Enter the 2nd number :")))
print("Number Number1 is greater than Number Number2" if number1 > number2 else
      "Number Number2 is greater than Number1" if number1 < number2 else "Botha are equal")

