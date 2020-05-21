"""
function_keyword_call
"""


def student_data( name, age ):
   # "function will print the info passed into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return


# function calling by default required parameters
# In this case, sequence must be followed for correct result
student_data("Sanjay", 22)

# Incorrect sequence will result in unexpected outcomes
student_data(22, "Sanjay")


# Function calling by keyword
# Here sequence does not matter
student_data( age = 22, name = "Sanjay" )


