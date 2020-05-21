"""
# Find and print the second maximum and second minimum number from a list
"""

A = [int(i) for i in input().split()]
A.sort()
print(A[len(A)-2], A[1])