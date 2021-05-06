n=int(input())
a=list(map(int,input().split()))

res=0
a.sort()
for i in range(n-1,1,-1):
    j=0
    k=i-1
    while(j<k):
        if(a[j]+a[k]==a[i]):
            res+=1
            j+=1
            k-=1
        elif(a[j]+a[k]<a[i]):
            j+=1
        else:
            k-=1
print(res)
