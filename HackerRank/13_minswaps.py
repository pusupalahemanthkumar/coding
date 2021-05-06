n=int(input())
a=list(map(int,input().split()))

i=res=0
while(i<n):
    index=a[i]-1
    if(a[i]!=a[index]):
        a[i],a[index]=a[index],a[i]
        res+=1
    else:
        i+=1
print(res)