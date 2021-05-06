n,m=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

def minPathSum(a,m,n):
    if(m==0):
        return 0
    dp=[[0 for i in range(m)] for j in range(n)]
    dp[0][0]=a[0][0]
    for i in range(1,m):
        dp[0][i]=dp[0][i-1]+a[0][i]
    for i in range(1,n):
        dp[i][0]=dp[i-1][0]+a[i][0]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j]=a[i][j]+min(dp[i-1][j],dp[i][j-1])
    return dp[n-1][m-1]
print(minPathSum(a,m,n))
