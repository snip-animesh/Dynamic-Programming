for _ in range(int(input())):
    n,amount=map(int,input().split())
    set_elems=[int(x) for x in input().split()]
    elements=set()
    dp=[1]+[0]*amount
    for i in set_elems:
        x=i
        for j in range(amount,x-1,-1):
            if dp[j]==0 and dp[j-i]!=0:
                dp[j]=i
        if dp[amount]:
            # print(1)
            break
    if dp[amount]==0:
        print(-1)
    else:
        i=amount
        while(i>0):
            print(dp[i],end=" ")
            i-=dp[i]
