# in built Function----------------------------
# int()
# str()
# bool()

#Module Function-------------------------------
# import math # all adad from math
# from math import sqrt #Partucular add from Math
# print(dir(math))
# print(sqrt(16))

#User Define Function----------------------------

# def function_name(Parameters):
#     //do Something
def print_sum(a,b=4):  # if not pass in calling function in b value then default take this 4 value of b
    print(a+b)
print_sum(5)