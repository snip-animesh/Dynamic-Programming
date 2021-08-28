def howSum(targetSum,numbers):
    table=[-1]*(targetSum+1)
    table[0]=[]
    for i in range(targetSum+1):
        if table[i]!=-1:
            for num in numbers:
                if i+num<=targetSum:
                    table[i+num]=table[i]+[num]
    return table[targetSum]

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))
