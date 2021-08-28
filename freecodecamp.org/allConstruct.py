# This is brute force function. 
def allConstruct(target, wordBank):

    if target=="":
        return [[]]
    totalWays=[]
    for word in wordBank:
        if target.startswith(word):
            totalWays+=[[word]+ suffix for suffix in allConstruct(target[len(word):],wordBank)]
    return totalWays

  
#   This is memoized function
def allConstruct(target, wordBank,memo=None):
    if memo==None:
        memo={}
    if target in memo:
        return memo[target]
    if target=="":
        return [[]]
    totalWays=[]
    for word in wordBank:
        if target.startswith(word):
            totalWays+=[[word]+ suffix for suffix in allConstruct(target[len(word):],wordBank,memo)]
    memo[target]=totalWays
    return totalWays

  
  """Complexity --> time O(n^m)
  space O(m)
  we can't do better than it"""

print(allConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(allConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
print(allConstruct("purple",["purp","p","ur","le","purpl"]))
print(allConstruct("enterapotentpot",["a","p","ent","enter","o","t","ot"]))
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee",
                                                      "eeeeee"]))
