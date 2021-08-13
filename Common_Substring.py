for _ in range(int(input())):
    s1=input()
    s2=input();maxi=0
    if s1==s2:
        print(0)
    else:
        m=len(s1);n=len(s2)
        lst=[[0 for i in range(m)] for i in range(n)]
#       lst=[[0]*m]*n এভাবে নিলে শ্যালো কপির একটা ঝামেলা হয় । ঝামেলা টা বুঝতে নিচে লিংক দিইয়ে দিলাম । 
        for j in range(n):
            for i in range(m):
                if s2[j]==s1[i]:
                    if i!=0 and j!=0:
                        lst[j][i]=lst[j-1][i-1]+1
                    else:
                        lst[j][i]=1
                    maxi=max(maxi,lst[j][i])
                else:
                    lst[j][i]=0
        print(m+n-(2*maxi))
        
'''This problem is about dynamic string and findng maximum length of common substring.
Shallow copy --> https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
Logic of Longest common substring --> https://www.youtube.com/watch?v=BysNXJHzCEs&t=76 ''' 
