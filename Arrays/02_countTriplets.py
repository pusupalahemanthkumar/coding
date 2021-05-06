n=int(input())
a=list(map(int,input().split()))

res=0
d=dict.fromkeys(set(a),0)
for i in range(n):
    d[a[i]]+=1
a.sort()
for i in range(n-1,1,-1):
    complement=a[i]-a[i-1]
    if(d.get(complement)):
        res+=1
print(res)