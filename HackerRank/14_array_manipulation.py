n,m=list(map(int,input().split()))
q=[]
for i in range(m):
    q.append(list(map(int,input().split())))
a=[0]*(n+2)
#print(q,a)

for i in range(m):
    s,e,k=q[i]
    #print(s,e,k)
    a[s]+=k
    a[e+1]-=k
    #print(a)
#print(a)
prev=a[0]
for i in range(1,len(a)):
    a[i]=prev+a[i]
    prev=a[i]
print(max(a))



