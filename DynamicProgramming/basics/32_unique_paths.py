n,m=list(map(int,input().split()))

def uniquePaths(n,m):
    dp=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if(i==0 or j==0):
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]
    
print(uniquePaths(n,m))