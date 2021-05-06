n=int(input())
a=list(map(int,input().split()))
s=int(input())

def backtracking(a,n,s):
    if(s==0):
        return 1
    if(n==0):
        return 0
    if(a[n-1]>s):
        return backtracking(a,n-1,s)
    else:
        return backtracking(a,n-1,s) + backtracking(a,n-1,s-a[n-1])

def count_subsets(a,n,s):
    dp=[[0 for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,s+1):
        dp[0][i]=0
    for i in range(1,n+1):
        for j in range(1,s+1):
            if(a[i-1]>j):
                dp[i][j]=dp[i-1][j]
            elif(a[i-1]<=j):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-a[i-1]]
    return dp[n][s]



print(backtracking(a,n,s))
print(count_subsets(a,n,s))