"""
function_keyword_call
"""


def student_data( name, age = 18 ):
   # "function will assume ass the students are adults. If age is specified
   # during the function call, that age will be considered
   print ("Name: ", name)
   print ("Age ", age)
   return


# Function calling with default argument
student_data("Sanjay")


# Function calling with specified argument
student_data("Sanjay", 22)
