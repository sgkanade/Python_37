"""

Using the Python map() function

"""

def my_square(x):    
    y = x * x    
    return y

numbers = (1, 2, 3, 4) 
# First way
y = []
for num in numbers:
    y.append(my_square(num))
print("Without using map function ", y)

# A better way
z = map(my_square,numbers) # map applies the my_square on the tuple numbers
                           # Each value in tuple is passed to the function 
print("After using map function ", list(z))