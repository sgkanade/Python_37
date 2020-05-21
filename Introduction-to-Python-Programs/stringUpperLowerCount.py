"""
stringUpperLowerCount
The function accepts a string and returns the number of lower case letters
and upper case letters

"""
def stringUpperLowerCount(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case letters : ", d["UPPER_CASE"])
    print ("No. of Lower case letters : ", d["LOWER_CASE"])

stringUpperLowerCount("I Love Python Programming")

stringUpperLowerCount(input("Enter your string - "))