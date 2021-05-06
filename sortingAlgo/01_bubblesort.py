n=int(input())
a=list(map(int,input().split()))

print("Before Sorting :")
print(a)
swapcont=0
for i in range(n):
    for j in range(0,n-i-1):
        if(a[j+1]<a[j]):
            t=a[j+1]
            a[j+1]=a[j]
            a[j]=t
            swapcont+=1
print("swapcount : {}".format(swapcont))
print(a)

