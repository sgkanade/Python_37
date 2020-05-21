"""
Using else with for loop
"""

my_list = [1,3,5,7,9,11,13,15]

for num in my_list:
    if num%2 == 0:
        print ('There an even number in the list')
        break
else:
    print ('There is NO even number in the list')
    
    
"""
Using else with while loop
"""
count = 1
while count < 11:
    print("The current count is: ",count)
    count  = count + 1 # increment the counter
else:
    print(count, " is now greater than 10")
    

   