n=int(input())
a=list(map(int,input().split()))

res=3e10
a.sort()
for i in range(len(a)-1):
    cur=abs(a[i]-a[i+1])
    res=min(cur,res)
print(res)