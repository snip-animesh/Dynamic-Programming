"""This is a probelm , link --> https://codeforces.com/contest/474/problem/D 
Logic from https://www.youtube.com/watch?v=O8rSLhIlj_I&t=716s"""

t,k=map(int,input().split())
def getAns(n,dp={}):
    ans = 0
    if n==0:
        return 1
    if n in dp:
        return dp[n]

    #W
    if n>=k:
        ans+=getAns(n-k,dp)
        ans=ans%1000000007
    #R
    ans+=getAns(n-1,dp)
    ans =ans% 1000000007
    dp[n]=ans
    return dp[n]

pre=[0]*100007
for i in range(1,100007):
    pre[i]=pre[i-1]+getAns(i)

for i in range(t):
    a,b=map(int,input().split())
    print((pre[b]-pre[a-1] + 1000000007) % 1000000007)
#     pre[b]-pre[a-1] could be negative .
