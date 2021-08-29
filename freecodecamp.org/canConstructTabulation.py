def canConstructTabu(target,wordBank):
    m=len(target)
    table=[False]*(m+1)
    table[0]=True
    for i in range(m):                             # m iteration here
        if table[i]:
            for word in wordBank:                  # n iteration here
                if target[i:].startswith(word):    # m iteration here
                    table[i+len(word)]=True
    return table[m]


print(canConstructTabu("abcdef",["ab","abc","cd","def","abcd"])) #true
print(canConstructTabu("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #False
print(canConstructTabu("enterapotentpot",["a","p","ent","enter","ot","o","t"])) #true
print(canConstructTabu("eeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee",
                                                        "eeeee","eeeeee"])) #false

# time O(m^2*n)
# space O(m)
