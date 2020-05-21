"""
function_variable_arguments
"""


def marksheet( avg_marks, *sub_marks ):
    """ This function takes average marks of a student. 
    Optionally, it takes subject wise marks also. 
    If subject-wise marks are also provided, it will print agerage marks 
    followed by subject-wise marks. 
    If only average marks are provided, it will print only average marks."""
    
    print ("Average Marks are : ")
    print (avg_marks)
    
    for marks in sub_marks :
        print ("Subject wise marks are : ", marks)
    return

# Now we can call marksheet function with single argument
marksheet( 60 )


# Now we can call marksheet function with additional arguments

marksheet( 60, 60, 50, 70 )