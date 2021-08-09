dp=[0]*1000000
mod=1000000007
dp[1]=1;dp[2]=2
for i in range(3,1000001):
    dp[i]=(dp[i-1]+dp[i-2])%mod
    
#This will take O(n) time to prepare this array ..
#From CodeNcode
