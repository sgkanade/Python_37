"""
factorial_recursion with recursion
"""

def fact_recursion(num):
    
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact_recursion(num - 1)
        

x = 6
y = fact_recursion(x) 
print("Factorial of {} is {}".format(x, y))