def countConstructTabu(target,wordBank):
    m=len(target)
    table=[0]*(m+1)
    table[0]=1
    for i in range(m):                             # m iteration here
        if table[i]:
            for word in wordBank:                  # n iteration here
                if target[i:].startswith(word):    # m iteration here
                    table[i+len(word)]+=table[i]
    return table[m]


print(countConstructTabu("abcdef",["ab","abc","cd","def","abcd"])) #1
print(countConstructTabu("purple",["purp","p","ur","le","purpl"])) #2
print(countConstructTabu("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #0
print(countConstructTabu("enterapotentpot",["a","p","ent","enter","ot","o","t"])) #4
print(countConstructTabu("eeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee",
                                                        "eeeee","eeeeee"])) #0
print(countConstructTabu("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #0
# time O(m^2*n)
# space O(m)
