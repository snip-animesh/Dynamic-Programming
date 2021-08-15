""" Given a rod of length N and you want to cut up the rod and sell the pieces in a way that maximizes the total amount of money you get. A piece of length i is worth price[i]
units of money."""
price=[0,1,5,8,9,10,17,17,20,24,30]
# price[i] is the price of length i rod
N=10
dp=[0]*(N+1)
for i in range(1,N+1):
    profit=0
    for j in range(1,i+1):
        profit=max(profit,price[j]+dp[i-j])
    dp[i]=profit
print(dp[N])

# Lecture 15 from CodeNCode
