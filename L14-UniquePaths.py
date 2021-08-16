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

# Here's the recursive approach I learnt from freecodecamp.org . It work's better .
def gridTraveller(m,n,memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[(m,n)]=gridTraveller(m-1,n,memo)+gridTraveller(m,n-1,memo)
    return memo[(m,n)]

print(gridTraveller(18,18))

dp=uniquePath()
print(dp)


# Logic from CodeNCode DP series L-14. 
# Practice Problem https://leetcode.com/problems/unique-paths/   and  https://leetcode.com/problems/unique-paths-ii/

"""UNIQUE PATH WITH OBSTACLES"""
# Practice Problem --> https://leetcode.com/problems/unique-paths-ii/
grid=[[0,0,0],[0,1,0],[0,0,0]]
m,n=len(grid),len(grid[0])
if grid[m-1][n-1]==1:
    print (0)
else:
    grid[m-1][n-1]=1
    for i in range(n-2,-1,-1):
        if grid[m-1][i]==0 and grid[m-1][i+1]==1:
            grid[m-1][i]=1
        else:
            grid [m-1][i]=0
    for i in range(m-2,-1,-1):
        if grid[i][n-1]==0 and grid[i+1][n-1]==1:
            grid[i][n-1]=1
        else:
            grid[i][n-1]=0

    for i in range(m-2,-1,-1):
        for j in range(n-2,-1,-1):
            if not grid[i][j]:
                grid[i][j]=grid[i+1][j]+grid[i][j+1]
            else:
                grid[i][j]=0
    print(grid[0][0])
