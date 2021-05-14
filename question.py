from sys import stdin
# input = lambda : stdin.readline().strip()
from math import ceil,sqrt,factorial,gcd
from collections import deque
from bisect import bisect_left
def beauty(n,m,s,x,y):
    d=[0 for i in range(n)]
    g={i:[] for i in range(n)}
    for i in range(m):
        x[i]-=1
        y[i]-=1
        g[x[i]].append(y[i])
        d[y[i]]+=1
    q=deque()
    for i in range(n):
        if d[i]==0:
            q.append(i)
    count=0
    res=0
    dp=[[0 for i in range(26)]for i in range(n)]
    while count<n and q:
        a=q.popleft()
        count+=1
        dp[a][ord(s[a])-97]+=1
        for i in g[a]:
            for j in range(26):
                dp[i][j]=max(dp[i][j],dp[a][j])
            d[i]-=1
            if d[i]==0:
                q.append(i)
    if count!=n:
        return -1
    else:
        res=0
        for i in range(n):
            res=max(res,max(dp[i]))
        return res

n,m=list(map(int,input().split()))
s=input()
x=list(map(int,input().split()))
y=list(map(int,input().split()))
print(beauty(n,m,s,x,y))
