# Task - Fibonacci series and Factorial
# # 3. Factorial
#
# # n = 5/
#
# # 5! -->5*4*3*2*1 -> 120
#
# # 3! -> 3*2*1 -> 6
#
# # 4! -> 4*3*2*1 -> 24

factorial = int(input("Enter the number :"))
num = 1
for i in range(1, factorial + 1):
    num = num * i
print("The factorial of given number is :",num)

# 3. Factorial

import math

number = int(input("Enter a number to calculate its factorial: "))

factorial = math.factorial(number)

print("Factorial of", number, "is", factorial)
