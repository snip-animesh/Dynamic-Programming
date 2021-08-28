def fibTab(n):
    table=[0]*(n+1)
    table[1]=1
    i,j,k=0,1,2
    while (k<=n+1):
        if k==n+1:
            table[j]+=table[i]
            break
        table[j]+=table[i]
        table[k]+=table[i]
        i+=1;j+=1;k+=1
    return table[n]


print(fibTab(50))

# Time and space Complexity O(n)
