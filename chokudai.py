sample="chokudai"
mod=10**9+7
inputed_string=input()
dp = [[0] * len(inputed_string) for _ in range(8)]
if inputed_string[0]==sample[0]:
    dp[0][0]=1
for i in range(1,len(inputed_string)):
    if sample[0]==inputed_string[i]:
        dp[0][i]+=(dp[0][i-1]+1)%mod
    else:
        dp[0][i]+=dp[0][i-1]
for i in range(1,8):
    for j in range(i,len(inputed_string)):
        if sample[i]==inputed_string[j]:
            dp[i][j]+=(dp[i-1][j-1]+dp[i][j-1])%mod
        else:
            dp[i][j]+=dp[i][j-1]
print(dp[7][len(inputed_string)-1])

# problem form atcoder.jp
