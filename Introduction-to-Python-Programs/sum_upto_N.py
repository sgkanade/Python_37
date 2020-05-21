"""
Factorial of a number (without using recursion)
"""




def sum_upto_N(num):
    """ This function calculates the sum up to num """
    total = 0
    for i in range(1,num+1):
        total = total + i
    return total
        
x = 7
y = sum_upto_N(x) 
print("Sum of all numbers up to {} is {}".format(x, y))