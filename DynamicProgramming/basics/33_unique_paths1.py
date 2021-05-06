n,m=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
def uniquePaths(a,m,n):
    dp=[[0 for i in range(m)] for j in range(n)]
    # rows
    flag=False
    for i in range(m):
        if(flag or a[0][i]==1):
            flag=True
            dp[0][i]=0
        else:
            dp[0][i]=1
    # cols
    flag=False
    for i in range(n):
        if(flag or a[i][0]==1):
            flag=True 
            dp[i][0]=0
        else:
            dp[i][0]=1 
    for i in range(1,n):
        for j in range(m):
            if(a[i][j]==1):
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[n-1][m-1] 
print(uniquePaths(a,m,n))


