"""Given a grid of size M*N , find number of unique path from cell (1,1) to (M,N) and you can go only down and right."""
# Mathematical approach -->
import math
x = math.factorial(m + n - 2)
y = math.factorial(m - 1)
z = math.factorial(n - 1)
print (x // (y * z))

# Iterative approach -->
m,n=map(int,input().split())
dp=[[1 for i in range(n)] for i in range(m)]
for i in range(m-2,-1,-1):
    for j in range(n-2,-1,-1):
        dp[i][j]=dp[i+1][j]+dp[i][j+1]
print(dp[0][0])

# Recursive approach

m,n=map(int,input().split())

def uniquePath(x=0,y=0):
    dp = [[-1 for i in range(n)] for i in range(m)]
    if x==m-1 or y==n-1:
        dp[x][y]=1
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=uniquePath(x+1,y)+uniquePath(x,y+1)
    return dp[x][y]


dp=uniquePath()
print(dp)

# Logic from CodeNCode DP series L-14. 
# Practice Problem https://leetcode.com/problems/unique-paths/   and  https://leetcode.com/problems/unique-paths-ii/
