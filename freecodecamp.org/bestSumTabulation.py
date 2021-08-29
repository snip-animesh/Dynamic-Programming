def bestSum(targetSum,numbers):
    table=[-1]*(targetSum+1)
    table[0]=[]
    for i in range(targetSum+1):
        if table[i]!=-1:
            for num in numbers:
                if i+num<=targetSum:
                    combination=table[i]+[num]
                    # if current combination is shorter than what already stored
                    if table[i+num] != -1 and len(combination)<len(table[i+num]):
                        table[i+num]=combination
                    #   if table[num+i]==-1 , then we will store combination there
                    elif table[i+num]==-1:
                        table[num+i]=combination
    return table[targetSum]

print(bestSum(7,[2,3]))
print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(100,[25,1,2,5]))


"""
n=len(numbers)
m=targetSum
complexity time O(m^2*n)
space(m^2)
"""
