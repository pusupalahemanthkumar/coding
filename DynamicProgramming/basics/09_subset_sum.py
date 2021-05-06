def backingTracking(a,n,s):
    if(s==0):
        return True
    if(n==0):
        return False
    if(a[n-1]>s):
        return backingTracking(a,n-1,s)
    return backingTracking(a,n-1,s) or backingTracking(a,n-1,s-a[n-1])

def isSubsetSum(a,n,s):
    subset=[[False for i in range(s+1)] for j in range(n+1)]

    for i in range(n+1):
        subset[i][0]=True
    for i in range(1,s+1):
        subset[0][i]=False


    for i in range(1,n+1):
        for j in range(1,s+1):
            if(j<a[i-1]):
                subset[i][j]=subset[i-1][j]
            if(j>=a[i-1]):
                subset[i][j]=subset[i-1][j] or subset[i-1][j-a[i-1]]
    for x in subset:
        print(x)
    return subset[n][s]

n,s=list(map(int,input().split()))
a=list(map(int,input().split()))
print(backingTracking(a,n,s))
print(isSubsetSum(a,n,s))
