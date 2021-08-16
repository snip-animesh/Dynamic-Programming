"""Given an integer array of size N , find subarray with maximum sum . 
A=[-1,-4,4,-2,0,1,4,-5]
ans =7 --> [4,-2,0,1,4] """

n=8
A=[-1,-4,4,-2,0,1,4,-5]
dp=[]
dp.append(A[0])
for i in range(1,n):
    dp.append(max(dp[i-1]+A[i],A[i]))
print(dp)

# It's also Cadane's algorithm . Logic from CodeNCode DP-1 Series .
# here's a practice problem --> https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/cricket-rating-30/
