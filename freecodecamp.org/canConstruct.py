def canConstruct(target,wordBank,memo=None):
    if memo==None:
        memo={}
    if target in memo:
        return memo[target]
    if target=="":
        return True
    for word in wordBank:                                   # n iteration here
        if target.startswith(word):                         # m iteration here
            suffix=target[len(word):]                       # m iteration here                    
            if canConstruct(suffix,wordBank,memo):
                memo[target]=True
                return True

    memo[target]=False
    return False


print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee",
                                                    "eeee","eeeee","eeeeee"]))

# m=target.length
# n=wordBank.length
# time O(m^2*n)
#space O(m)
