def stair(n):
    if n==1 or n==2 :
        return n
    res=0
    res+=stair(n-1)
    res+=stair(n-2)
    return res

for i in range(int(input())):
    print(stair(int(input())))
    
#     This is not efficient

import sys
sys.setrecursionlimit(100007)

dp=[0]*1000001
def stair(n):
    if n==1 or n==2 :
        return n
    elif dp[n] !=0:
        return dp[n]
    dp[n]=stair(n-1)+stair(n-2)
    return dp[n]


for i in range(int(input())):
    print(stair(int(input())))
    
#     This is efficient but gets memory error .. 


# This code from CodeNCode 
import sys
sys.setrecursionlimit(100007)


def fib(n,memo={}):
    if n in memo:
        return memo[n]
    elif n<=2:
        return 1
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]



print(fib(1000))
