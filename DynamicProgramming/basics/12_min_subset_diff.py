n=int(input())
a=list(map(int,input().split()))

def min_subset_diff(a,n):
    s=0
    for i in a:
        s+=i 
    dp=[[False for i in range(s+1)] for j in range(n+1)]

    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,s+1):
        dp[0][i]=False 
    for i in range(1,n+1):
        for j in range(1,s+1):
            if(a[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-a[i-1]]
    
    diff=s 
    for i in range((s//2)+1):
        first=i 
        second=s-i
        if(dp[n][i]==True and diff >abs(first-second)):
            diff=abs(first-second)
    return diff  
print(min_subset_diff(a,n))