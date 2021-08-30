def getAns(posCurrentMarbel, posPreviousPinnedMarbel, memo=None):
    if memo == None:
        memo={}
    if (posCurrentMarbel, posPreviousPinnedMarbel) in memo:
        return memo[(posCurrentMarbel, posPreviousPinnedMarbel)]
    if posCurrentMarbel > n - 1: return 0  # if we are beyond rightmost marbel then it won't cost anythig
    # cost of pinning
    x = lst[posCurrentMarbel][1] + getAns(posCurrentMarbel + 1, posCurrentMarbel, memo)
    # cost of leaving
    y = abs(lst[posCurrentMarbel][0] - lst[posPreviousPinnedMarbel][0]) + getAns(posCurrentMarbel + 1,
                                                                                 posPreviousPinnedMarbel, memo)
    memo[(posCurrentMarbel, posPreviousPinnedMarbel)] = min(x, y)
    return memo[(posCurrentMarbel, posPreviousPinnedMarbel)]


lst = [];
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
lst.sort()
ans = lst[0][1]
if n > 1:
    ans += getAns(1, 0)
print(ans)


# This get TLE
