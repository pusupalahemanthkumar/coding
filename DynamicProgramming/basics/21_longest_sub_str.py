s1,s2=input().split()

def lcs(s1,s2,m,n):
    dp=[[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[m][n]
def findLCS(s1,s2):
    len1=len(s1)
    len2=len(s2)
    dp=[["" for i in range(len2+1)] for j in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if(i==0 or j==0):
                dp[i][j]=""
            elif(s1[i-1]==s2[j-1]):
                dp[i][j]=dp[i-1][j-1]+s1[i-1]
            else:
                t=len(dp[i][j-1]) >len(dp[i-1][j])
                dp[i][j]=dp[i][j-1] if t else dp[i-1][j]
    return dp[len1][len2]

print(lcs(s1,s2,len(s1),len(s2)))
print(findLCS(s1,s2))