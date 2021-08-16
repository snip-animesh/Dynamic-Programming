"""Given n integers , find what is the minmum integer you cannot make using any subset of given array.
Example - 
A=[1,2,5]
ans=5"""


n=int(input())
A=[int(x) for x in input().split()]
x=0
for i in range(n):
    if A[i]>x+1:
        break
    else:
        x+=A[i]
print(x+1)

# Logic from CodeNCode , DP-1 series lecture 17
