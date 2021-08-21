string=input()
l=len(string)
e=[-1]*l
F=[0]*(l+1)
stack=[]
maxi=0
for i in range(l):
    if string[i]=="(":
        stack.append(i)
    else:
        if len(stack)!=0:
            last_index=stack.pop()
            if last_index ==0:
                e[i]=0
                F[i-e[i]+1]+=1
                maxi=max(maxi,i-e[i]+1)
            else:
                if e[last_index-1]!=-1:
                    e[i]=e[last_index-1]
                    F[i-e[i]+1]+=1
                    maxi=max(maxi,i-e[i]+1)
                else:
                    e[i]=last_index
                    F[i-e[i]+1]+=1
                    maxi=max(maxi,i-e[i]+1)
if maxi==0:
    print(0,1)
else:
    print(maxi,F[maxi])


"""This is a problem from codeforces . https://codeforces.com/contest/5/problem/C 
Logic from CodeNCode"""
