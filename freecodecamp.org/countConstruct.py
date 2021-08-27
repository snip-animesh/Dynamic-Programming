def countConstruct(target, wordBank,memo=None):
    if memo==None:
        memo={}
    if target in memo:
        return memo[target]
    cnt=0
    if target=="":
        return 1
    for word in wordBank:
        try:
            if target.index(word)==0:
                suffix=target[len(word):]
                cntWaysForRest=countConstruct(suffix,wordBank,memo)
                memo[target]=cntWaysForRest
                cnt+=cntWaysForRest
        except:
            continue
    # memo[target]=cnt
    return cnt


print(countConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(countConstruct("purple",["purp","p","ur","le","purpl"]))
print(countConstruct("enterapotentpot",["a","p","ent","enter","o","t","ot"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee",
                                                      "eeeeee"]))

"""
time complexity --> O(n*m^2)
space--> O(m^2)
"""
