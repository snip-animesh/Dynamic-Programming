def howSum(targetsum,numbers,memo=None):
    if memo==None:
        memo={}
    if targetsum==0:
        return []
    if targetsum in memo:
        return memo[targetsum]
    if targetsum <0:
        return None
    for num in numbers:
        remainder=targetsum-num
        remainderResult=howSum(remainder,numbers,memo)
        if remainderResult!=None:
            memo[targetsum]=[*remainderResult,num]
            return memo[targetsum]
    memo[targetsum]=None
    return None


print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(28,[14,7]))

# Logic from freecodecamp.org
