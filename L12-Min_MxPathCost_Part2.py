# Given a grid of size row*col . Find a path from any cell in first row to any cell in the last row which minimize the cost. 
# You Can go down, down-right, down-left .
inf=1000000000

row,col=map(int,input().split())
main_array=[]
for i in range(row):
    lst=[int(x) for x in input().split()]
    main_array.append(lst)
dp=[[inf for i in range(col+2)] for j in range(row)]
# Copying the last row of main_array to dp array.
for i in range(col):
    dp[row-1][i+1]=main_array[row-1][i]

for i in range(row-2,-1,-1):
    for j in range(col,0,-1):
        dp[i][j]=main_array[i][j-1]+ min(dp[i+1][j],dp[i+1][j+1],dp[i+1][j-1])
print(min(dp[0]))

# Given a grid of size row*col . Find a path from any cell in first row to any cell in the last row which maximizing the cost. 
# You Can go down, down-right, down-left .

inf=-1000000000

row,col=map(int,input().split())
main_array=[]
for i in range(row):
    lst=[int(x) for x in input().split()]
    main_array.append(lst)
dp=[[inf for i in range(col+2)] for j in range(row)]
# Copying the last row of main_array to dp array.
for i in range(col):
    dp[row-1][i+1]=main_array[row-1][i]

for i in range(row-2,-1,-1):
    for j in range(col,0,-1):
        dp[i][j]=main_array[i][j-1]+ max(dp[i+1][j],dp[i+1][j+1],dp[i+1][j-1])
print(max(dp[0]))
