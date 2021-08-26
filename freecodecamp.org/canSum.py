def canSum(target,numbers,memo=None):
    if memo==None:
        memo={}
    if target in memo:
        return memo[target]
    if target==0:
        return True
    if target<0:
        return False
    for num in numbers:
        remainder=target-num
        if canSum(remainder,numbers,memo):
            memo[target]=True
            return True
    memo[target]=False
    return memo[target]


print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(8,[2,3,5]))
print(canSum(3000,[7,14]))

# time O(m*n) 
# space O(m)
