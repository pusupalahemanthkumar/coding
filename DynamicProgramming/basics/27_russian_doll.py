
def maxEnvelopes(a,n):
    if(n==0):
        return 0 
    a.sort(key=lambda x:(x[0],-x[1]))
    print(a)
    dp=[1]*(n+1)
    
    for i in range(1,n):
        for j in range(0,i):
            if(a[i][0]>a[j][0] and a[i][1]>a[j][1] and dp[i]<1+dp[j]):
                dp[i]=1+dp[j]
    print(dp)
    max=1
    for i in dp:
        if(i>max):
            max=i 
    return max
    
    



# (w,h)
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
print(maxEnvelopes(a,n))
"""
4
5 4
6 4
6 7
2 3
"""
