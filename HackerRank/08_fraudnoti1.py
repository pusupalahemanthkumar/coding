import bisect

n,d=list(map(int,input().split()))
a=list(map(int,input().split()))

# current window
curw=sorted(a[0:d])
print(curw)
m=d//2

def med(arr,d,m):
    if(d%2==0):
        return (arr[m-1]+arr[m])/2
    else:
        return arr[m]
res=0
for i in range(d,n):
    if(a[i]>=2*med(curw,d,m)):
        res+=1
    del curw[bisect.bisect_left(curw,a[i-d])]
    bisect.insort(curw,a[i])
print(res)

