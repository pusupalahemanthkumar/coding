def result(a,n):
    res=0
    for i in range(1,n-1):
        if(a[i-1]<a[i]):
            res+=a[i]-a[i-1]
    return res
n=int(input())
a=list(map(int,input().split()))
print(result(a,n))