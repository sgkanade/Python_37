
"""
Sum of all elements in a list
"""

def sumOfList(list1):
    sum = 0
    for num in list1:
        sum = sum + num
    return sum

input_list = input("Enter a list of integers => ")
integer_list = list(map(int, input_list.split()))
total = sumOfList(integer_list)
print("Sum of the list elements is = ",total)