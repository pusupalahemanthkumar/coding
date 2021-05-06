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

def shortestCommon(s1,s2):
    ans=""
    lcs=findLCS(s1,s2)
    p1=p2=0
    for c in lcs:
        while(p1<len(s1) and s1[p1]!=c):
            ans+=s1[p1]
            p1+=1
        while(p2<len(s2) and s2[p2]!=c):
            ans+=s2[p2]
            p2+=1
        ans+=c 
        p1+=1
        p2+=1
    return ans+s1[p1:]+s2[p2:]
s1,s2=input().split()
print(shortestCommon(s1,s2))