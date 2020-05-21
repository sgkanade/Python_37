# -*- coding: utf-8 -*-
"""
Factorial of a number (without using function)
"""


n = int(input("Enter a number which you want to calculate factorial of : "))
fact = 1
if n == 0:
    print(fact)
else:
    for i in range(1,n+1):
        fact = fact * i
print(fact,end="")