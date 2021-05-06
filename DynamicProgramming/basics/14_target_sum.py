n=int(input())
a=list(map(int,input().split()))
t=int(input())

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
def count_target(a,n,t):
    s=0
    for i in a:
        s+=i 
    t=(s+t)//2
    return count_subsets(a,n,t)

print(count_target(a,n,t))


