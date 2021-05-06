from collections import deque

def median(f=deque()):
    f=sorted(f)
    n=len(f)
    medianv=0
    if(n%2!=0):
        medianv=f[n//2]
    else:
        m=n//2
        medianv=(f[m]+f[m+1])/2
    return medianv

n,d=list(map(int,input().split()))

a=list(map(int,input().split()))
f=deque()
# first window
for i in range(d):
    f.append(a[i])
m=median(f)
print(f,m)
res=0
for i in range(d,n):
    print(i,a[i],2*m)
    if(a[i]>=2*m):
        res+=1
    f.popleft()
    f.append(a[i])
    m=median(f)
    print(f,m)
print(res)


