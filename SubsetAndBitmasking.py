s=['A','B','C','D']
t=int(input())
while t:
    n=int(input())
    tot=1<<n
    for N in range(tot):
        for j in range(n):
            f=1<<j
            if N & f:
                print(s[j],end=" ")
        print()

    t-=1
    
    
#    L-04 from CodeNcode
   
