def backingTracking(a,n,s):
    if(s==0):
        return True
    if(n==0):
        return False
    if(a[n-1]>s):
        return backingTracking(a,n-1,s)
    return backingTracking(a,n-1,s) or backingTracking(a,n-1,s-a[n-1])

def findPartion(a,n):
    s=0
    for i in a:
        s+=i
    if(s & 1):
        return False

    return backingTracking(a,n,s//2)

n=int(input())
a=list(map(int,input().split()))
print(findPartion(a,n))