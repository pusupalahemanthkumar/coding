def result(a,n):
    if(n==0 or n==1):
        return n
    i=0
    for j in range(1,n):
        if(a[j]!=nums[i]):
            i+=1
            a[i]=a[j]
    return i+1


n=int(input())
a=list(map(int,input().split()))

l=result(a,n)
for i in range(l):
    print(a[i],end=" ")