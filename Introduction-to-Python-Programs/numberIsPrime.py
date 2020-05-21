"""
numberIsPrime - a function to check if a number is prime

"""


def numIsPrime(num):
    if num > 1: 
        # Iterate from 2 to n / 2  
        for i in range(2, num//2): # this is floor division
            
            # If num is divisible by any number between  
            # 2 and n / 2, it is not prime  
            if (num % i) == 0: 
                return "NOT PRIME"
                #print(num, "is not a prime number") 
                #break
            else: 
                return "PRIME"
                #print(num, "is a prime number") 
                
    else: 
        return "NOT PRIME"
        #print(num, "is not a prime number") 
   

x = 23
result = numIsPrime(x)
print("The number {} is {}".format(x,result))