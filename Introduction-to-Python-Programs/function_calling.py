"""
function_calling

If you modify a list inside a function, 
then it is reflected in the reference list also

"""

def changeme( mylist ):
   print ("Inside function before change: ", mylist)
   
   mylist[0] = 40 # This will update the list in original reference
   print ("Inside function after change: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
print ("Outside the function before change: ", mylist)
changeme( mylist )
print ("Outside the function after change: ", mylist)
 

