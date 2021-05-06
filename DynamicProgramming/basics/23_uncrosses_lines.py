a=list(map(int,input().split()))
b=list(map(int,input().split()))

def maxUncrossedLines(a,b):
    len1=len(a)
    len2=len(b)
    dp=[[0 for i in range(len2+1)] for j in range(len1+1)]

    for i in range(len1+1):
        for j in range(len2+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(a[i-1]==b[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[len1][len2]

print(maxUncrossedLines(a,b))
