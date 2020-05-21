"""
for Loops
"""

a = list(range(10))  # range starts from 0 ends at <given number>-1; here upto 9
print(a)

# This loop will print values from 0 to 9
for i in range(10): # i will take values from 0 to 9
    print(i)

for j in range(1,11):
    print(j)

seq1 = ['a','b','c','d','e'] # define a list of characters

for item in seq1: # item will take one-by-one value from seq
    print(item) # this will print items one-by-one

for jelly in seq1: # jelly is a variable here which will take one-by-one ...
                  #  values from seq
    print(jelly+jelly)

String = 'Python'
for letter in String:
    print("Letter in String is: ", letter)

seq2 = ['abc','def','ghi','jkl','mnp'] # define a list of strings

for item in seq2: # item will take one-by-one value from seq
    print(item) # this will print items one-by-one


# Another way to print items from a list is by using iterating the sequence index
length_seq2 = len(seq2) # find length of the seq2
for index in range(length_seq2):
    print(seq2[index])

# while loop

count = 1
while count < 11:
    print("The current count is: ",count)
    count  = count + 1 # increment the counter


# infinite while loop
    
i = 1
while i == 1 :  # This condition is always True, hence loop will never exit
   j = int(input("What is your number :"))
   print ("Your number is : ", j)
   print("You are in an infinite loop! Press CTRL+C to terminate this loop.")

print ("Loop terminated!")
