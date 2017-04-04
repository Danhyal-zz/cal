import math
import random
import sys
import os
import time



operation = input('''
please enter the operator you would like to use:
+ for addition
- for subtraction
/ for division
x for muliply
r to find the remainder of a division
:''')


number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))

if operation == "x":
    print('{} X {} = '.format(number_1, number_2))

    print(number_1 * number_2)

elif operation == "+":
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == "-":
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == "/":
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

elif operation == "r":
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 % number_2)


else:
    print("Please use the operators listed above")


