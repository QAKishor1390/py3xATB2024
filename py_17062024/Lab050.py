#   Functions :
#   Block of code - which can executed or reused.
#   Define
#   Call

# Builtin Functions - bultins.py - file (Python 3 setup)
# Which are created by the python contributers

result = max(2, 3)
print(result)


# User Defined
# They can return something
# They can't return  -> non return
# They have parameters
# They don't parameters / arguments


# def say_hello():  # Define function // No Return Type and No Parameter/Argument
#     print("Hello,Welcome to Python")
#
#
# say_hello()  # Call the function
#
#
# def say_hello_arg(name):  # No return type and with argument
#     print("Hello", name)
#
#
# say_hello_arg("Kishor")
# say_hello_arg("Nitya")

def say_hello_default(name="Kishor"):  # No return type and with default argument
    print("Hello", name)


say_hello_default()
say_hello_default("Isha")
say_hello_default(name="Yami")


# argumrnt + return type

def sum_number_arg_ret(a, b):
    return a + b


result = sum_number_arg_ret(7, 7)
result = sum_number_arg_ret(a=44, b=88)
print(result)
