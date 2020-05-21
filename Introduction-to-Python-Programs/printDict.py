"""
Print dictionary

Given an integer number n, 
define a function named printDict() 
which can print a dictionary where the keys are numbers 
between 1 and n (both included) and the values are square of the keys

"""

def printDict():
    N = int(input("Enter a number n "))
    dict1 = {}
    for i in range (1,N+1):
        dict1[i] = i*i
    print(dict1)

printDict() # We are calling the function without any arguments
            # Also, the function is not returning anything