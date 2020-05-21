"""
function_calling_2

If you assign a list to a variable, then a new local variable is created, 
without altering the original variable

"""



# 
def changeme( mylist ):
   print ("Inside function before change: ", mylist)
   mylist = [1,2,3,4] # This would assign new reference in mylist
   print ("Inside function after change: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
print ("Outside the function before change: ", mylist)
changeme( mylist )
print ("Outside the function after change: ", mylist)