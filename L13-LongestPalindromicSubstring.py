s=input()
l=len(s)
dp=[[0 for i in range(l+1)] for j in range(l+1)]
for _ in range(2):
    for i in range(_,l+1):
        dp[_][i]=1
max_subs=1 #maximum length of substring
max_col=1 #taking value of column to find the longest substring
for i in range(2,l+1):
    for j in range(i,l+1):
        if s[j-1]==s[j-i] and dp[i-2][j-1]==1:
            dp[i][j]=1
            max_subs=i
            max_col=j
print(max_subs)
print(s[max_col-max_subs:max_col])

# This is to find the longest common substring o a given string and the substring .
# Logic from CodeNCode
# Practice from https://leetcode.com/problems/longest-palindromic-substring/submissions/
