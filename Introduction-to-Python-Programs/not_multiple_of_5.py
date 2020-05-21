# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:06:02 2020

@author: Kirti
"""


A = [int(i) for i in input().split()]
for i in range(len(A)):
	if (A[i]%5!=0):
		if (i != len(A)-1):
			print(A[i],end=" ")
		else:
			print(A[i],end="")