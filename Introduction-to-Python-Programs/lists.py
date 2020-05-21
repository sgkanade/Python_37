
# Lists


my_list_1 = ['hi',1,[1,2]] # List with items of different data types

my_list_2 = ['a','b','c']  # List with items of same data types

my_list_2.append('d') # Append the list with an item

print(my_list_2) # Print a list

print(my_list_2[0]) # Extract the first item in the list

print(my_list_2[1]) # Extract the second item in the list

print(my_list_2[1:]) # Extract items from index 1 onwards

print(my_list_2[:3]) # Extract all items upto index 3-1

my_list_2[0] = 'NEW' # Re-assign value 'NEW' to first item in list

print(my_list_2)

nested_list = [1,2,3,[4,5,['Python']]] # Nested list - having lists as items in a list

print(nested_list[3]) # Extract 4th item in the list

print(nested_list[3][2]) # Extract third item of fourth item of list

print(nested_list[3][2][0][2])
 
