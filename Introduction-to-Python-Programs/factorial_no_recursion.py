"""
Factorial of a number (without using recursion)
"""




def fact_no_recursion(num):
    fact = 1
    if num == 0:
        return fact
    else:
        for i in range(1,num+1):
            fact = fact * i
        return fact
        

x = 7000
y = fact_no_recursion(x) 
print("Factorial of {} is {}".format(x, y))