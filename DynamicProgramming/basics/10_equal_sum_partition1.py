
def isSubsetSum(a,n,s):
    subset=[[False for i in range(s+1)] for j in range(n+1)]

    for i in range(n+1):
        subset[i][0]=True
    for i in range(1,n+1):
        subset[0][i]=False


    for i in range(1,n+1):
        for j in range(1,s+1):
            if(j<a[i-1]):
                subset[i][j]=subset[i-1][j]
            if(j>=a[i-1]):
                subset[i][j]=subset[i-1][j] or subset[i-1][j-a[i-1]]
    return subset[n][s]

def findPartion(a,n):
    s=0
    for i in a:
        s+=i
    if(s & 1):
        return False

    return isSubsetSum(a,n,s//2)

n=int(input())
a=list(map(int,input().split()))
print(findPartion(a,n))