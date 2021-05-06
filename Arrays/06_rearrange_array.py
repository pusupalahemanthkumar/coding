n=int(input())
a=list(map(int,input().split()))

me=max(a)+1
maxi,mini=n-1,0
for i in range(n):
    if(i%2==0):
        a[i]=a[i]+a[maxi]%me*me
        maxi-=1
    else:
        a[i]=a[i]+a[mini]%me*me
        mini+=1
for i in range(n):
    a[i]=int(a[i]//me)
print(*a)
