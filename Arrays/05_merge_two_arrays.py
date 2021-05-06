import bisect

def result(a,b,n,m):
    i=j=0
    while(i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            i+=1
        elif(a[i]>b[j]):
            t=a[i]
            a[i]=b[j]
            del b[bisect.bisect_left(b,b[j])]
            bisect.insort(b,t)

n,m=list(map(int,input().split()))

a=list(map(int,input().split()))
b=list(map(int,input().split()))

result(a,b,n,m)

print(*a,end=" ")
print(*b,end=" ")
