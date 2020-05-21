"""
Print sum of elements of array and reverse of array
"""

N = int(input("Enter size of array : "))
A = [int(i) for i in input("Enter the elements of array separated by space : ").split(" ")]
B = []
for i in range(len(A)-1, -1,-1):
    B.append(A[i])
C = []
for i in range(len(B)):
    C.append(A[i]+B[i])
for i in range(len(C)):
    if(i==len(C)-1):
        print(C[i])
    else:
        print(C[i],end=" ")

        
# Another way        
N = int(input("Enter size of array : "))
A = [int(i) for i in input("Enter the elements of array separated by space : ").split()]
B = A.copy()
A.reverse();
C=list();
for j in range(N):
    C.append(int(A[j]) + int(B[j]))

for i in range(N):
    if (i < N-1):
        print(C[i],end=" ")
    else:
        print(C[i],end="")
        
