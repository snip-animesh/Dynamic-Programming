for _ in range(int(input())):
    n,amount=map(int,input().split())
    set_elems=[int(x) for x in input().split()]
    dp=[[0 for i in range(amount+1)] for j in range(n)]
    for i in range(n):
        for j in range(0,amount+1):
            if j==0:
                dp[i][j]=1  #1st column is always true
            elif j<set_elems[i]:
                if i==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]
            elif j==set_elems[i]:
                dp[i][j]=1
            else:
                if i==0:
                    dp[i][j]=0
                elif dp[i-1][j]==1:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j-set_elems[i]]
    print(dp[n-1][amount])

    #Below code is to show which elements are enough to make amount .
    elements=set(); i,j=n-1,amount
    while i!=0 or j!=0:
        if dp[i][j]==1:
            i-=1
        else:
            elements.add(set_elems[i+1])
            j-=set_elems[i+1]
    print(elements)
# Time and Space Complexity O(N*M)
# Best Explanation -https://www.youtube.com/watch?v=s6FhG--P7z0
# Lecture 08 from CodeNCode.



# Here's the code in from freecodecamp , implemented in recursive way .
def canSum(target,numbers,memo=None):
    if memo==None:
        memo={}
#In Python, when passing a mutable value as a default argument in a function, the default argument is mutated anytime that value is mutated.
# My memo dictionary was being mutated every call. So I simply changed memo=None and added a check to see if it was the first call of the function.

    if target in memo:
        return memo[target]
    if target==0:
        return True
    if target<0:
        return False
    for num in numbers:
        remainder=target-num
        if canSum(remainder,numbers,memo):
            memo[target]=True
            return True
    memo[target]=False
    return memo[target]


print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(3000,[7,14]))
