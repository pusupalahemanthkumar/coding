s=input()
def longestRepeatingSubSeq(s):
    a=s
    b=s
    len1=len(a)
    len2=len(b)
    dp=[["" for i in range(len2+1)] for j in range(len1+1)]

    for i in range(len1+1):
        for j in range(len2+1):
            if(i==0 or j==0):
                dp[i][j]=""
            elif(a[i-1]==b[j-1] and i !=j):
                dp[i][j]=dp[i-1][j-1]+a[i-1]
            else:
                t=len(dp[i-1][j])>len(dp[i][j-1])
                dp[i][j]+=dp[i-1][j] if t else dp[i][j-1]
    for x in dp:
        print(x)
    return dp[len1][len2]

print(longestRepeatingSubSeq(s))