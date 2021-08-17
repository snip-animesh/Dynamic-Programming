def getAns(n,f,h,k1,k2,memo={}):
    if n==0:
        return 1
    if (n,f,h,k1,k2) in memo:
        return memo[(n,f,h,k1,k2)]
    # fill f
    x=0
    if f>0 and k1>0:
        x=getAns(n-1,f-1,h,k1-1,limit_h,memo)
    # fill h
    y=0
    if h>0 and k2>0:
        y=getAns(n-1,f,h-1,limit_f,k2-1,memo)
    memo[(n,f,h,k1,k2)]=(x+y)%100000000
    return memo[(n,f,h,k1,k2)]

while True:
    n1,n2,limit_f,limit_h=map(int,input().split())
    print(getAns(n1+n2,n1,n2,limit_f,limit_h))
    
"""Logic from Code NCode , DP series Part 2 , lecture 1 . 
problem link --> https://codeforces.com/contest/118/problem/D
Breif description  of the logic on my notebook"""
