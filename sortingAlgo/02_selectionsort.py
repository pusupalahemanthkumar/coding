n=int(input())
a=list(map(int,input().split()))

swapcount=0
print("Before Sorting :")
print(a)
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
            swapcount+=1

print("swapcount : {}".format(swapcount))
print(a)