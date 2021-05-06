# https://practice.geeksforgeeks.org/problems/b6b608d4eb1c45f2b5cace77c4914f302ff0f80d/1/?track=MD-Math&batchId=144#

a=list(map(int,input().split()))

def smallestPositive(a):
    n=len(a)
    a.sort()
    res=0
    for i in range(n):
        if(a[i]<=res):
            res+=a[i]
        else:
            return res 
    return res
print(smallestPositive(a))
