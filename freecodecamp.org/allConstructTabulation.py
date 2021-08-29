def allConstructTabu(target,wordBank):
    m=len(target)
    table=[[] for _ in range(m+1)]
    table[0]=[[]]
    for i in range(m):                                          # m iteration
        if len(table[i]):
            for j in table[i]:                                  # This will be (n^m)
                for word in wordBank:
                    if target[i:].startswith(word):
                        table[i+len(word)].append(j+[word])
    return table[m]


print(allConstructTabu("abcdef",["ab","abc","cd","def","abcd","ef","c"])) #4
print(allConstructTabu("purple",["purp","p","ur","le","purpl"])) #2
print(allConstructTabu("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #0
print(allConstructTabu("enterapotentpot",["a","p","ent","enter","ot","o","t"])) #4
print(allConstructTabu("eeeeeeef",["e","ee","eee","eeee",
                                                        "eeeee","eeeeee"])) #0
print(allConstructTabu("skateboard",["bo","rd","ate","t","ska","sk","boar"])) #0
# time O(n^m)
# space O(n^m)
