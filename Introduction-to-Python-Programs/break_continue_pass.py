# -*- coding: utf-8 -*-
"""
break statement
"""

# This loop will run only till the index is 1. When index becomes 2, 
# the loop terminates
seq2 = ['abc','def','ghi','jkl','mnp']
length_seq2 = len(seq2) # find length of the seq2
for index in range(length_seq2):
    if index == 2:
        print("The index is now 2. I will terminate using break")
        break
    print("Index is ",index, "value is ", seq2[index])

input()
# This while loop will terminate when count becomes 5
count = 1
while count < 11:
    print("The current count is: ",count)
    count  = count + 1 # increment the counter
    if count == 5:
        print("The count is now 5. I will terminate using break")
        break
input()    
""" 
continue statement
"""
seq2 = ['abc','def','ghi','jkl','mnp']
length_seq2 = len(seq2) # find length of the seq2
for index in range(length_seq2):
    if index == 2:
        print("The index is now 2. I will skip the corresponding value")
        continue
    print("Index is ",index, "value is ", seq2[index])

input()

count = 0
while count < 11:
    count  = count + 1 # increment the counter
    if count == 5:
        print("The count is now 5. I will skip this value")
        continue    
    print("The current count is: ",count)