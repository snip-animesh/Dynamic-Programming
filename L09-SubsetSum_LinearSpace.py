for _ in range(int(input())):
    n,amount=map(int,input().split())
    set_elems=[int(x) for x in input().split()]
    dp=[1]+[0]*amount
    for i in set_elems:
        x=i
        for j in range(amount,x-1,-1):
            if dp[j-i]==1:
                dp[j]=1
        if dp[amount]==1: 
            print(1)
            break
    # We need to check only weather dp[amount] true or false . So, if dp[amount] is True
    # we are getting out from the loop.
    else:
        print(0)

# Time Complexity O(N*amount)
# Space O(amount)
# Dedicated problem -->https://www.codechef.com/problems/TF01
# Logic from CodeNCode
