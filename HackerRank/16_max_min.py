n,k=int(input()),int(input())
a=[]
for i in range(n):
    a.append(int(input()))

a.sort()
print(a)

res=a[k-1]-a[0]
print(res)
for i in range(k,len(a)):
    t=a[i]-a[i-k+1]
    print(a[i],a[i-k+1])
    print(i,t,res)
    res=min(res,t)
    print(i,res)
print(res)