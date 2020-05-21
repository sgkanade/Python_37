# -*- coding: utf-8 -*-
"""
Calculate income tax for given salary

Slabs: Upto 3,00,000: NIL
        3,00,001 to 5,00,000: 5 %
        5,00,001 to 10,00,000: 20 %
        10,00,001 onwards: 30 %

"""

salary = int(input("Enter your salary = "))

if salary <= 300000:
    tax = 0
elif salary > 300000 and salary <= 500000:
    tax = salary*0.05
elif salary > 500000 and salary <= 1000000:
    tax = salary*0.2
else:
    tax = salary*0.3
    
print("Your salary is {} and the calcualted tax is {}".format(salary,tax))