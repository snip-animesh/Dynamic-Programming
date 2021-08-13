# Statement-Given a grid of size row*col , find a path from cell (1,1) to (row,col) which minimize the cost.
# Condition-You can go right or down only.
inf=1000000000
#Reading input
row,col=map(int,input().split())
main_array=[]
for i in range(row):
    lst=[int(x) for x in input().split()]
    main_array.append(lst)
dp=[[inf for i in range(col+1)] for j in range(row+1)]
dp[row][col-1],dp[row-1][col]=0,0

for i in range(row-1,-1,-1):
    for j in range(col-1,-1,-1):
        dp[i][j]=main_array[i][j]+ min(dp[i+1][j],dp[i][j+1])
print(dp[0][0])



# Statement-Given a grid of size row*col , find a path from cell (1,1) to (row,col) which maximize the cost.
# Condition-You can go right or down only.
inf=-1000000000
row,col=map(int,input().split())
main_array=[]
for i in range(row):
    lst=[int(x) for x in input().split()]
    main_array.append(lst)
dp=[[inf for i in range(col+1)] for j in range(row+1)]
dp[row][col-1],dp[row-1][col]=0,0

for i in range(row-1,-1,-1):
    for j in range(col-1,-1,-1):
        dp[i][j]=main_array[i][j]+ max(dp[i+1][j],dp[i][j+1])
print(dp[0][0])
