# 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#
# Use an if-else statement to make this determination.
#
# Input = 2024
# Output = Leap year


year= int(input("Enter the year :"))
if year % 4==0 and year % 100!=0:
    print(year, "Given Year is Leep Year")
elif year % 400 == 0:
    print(year,"Given year is leep year")
elif year % 100 !=0 :
    print(year,"Given year is not leep year")

