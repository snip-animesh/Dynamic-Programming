coins=[int(x) for x in input().split()]
coins.sort()
amount=int(input())
dp=[10**8]*(amount+1)
dp[0]=0
for i in range(1,amount+1):
    x=10**8
    for j in coins:
        if j<=i:
            x=min(x,dp[i-j])
        else:
            break
    if x==10**8:
        dp[i]=x
    else:
        dp[i]=x+1
if dp[amount]==10**8:
    print(-1)
else:
    print(dp[amount])
