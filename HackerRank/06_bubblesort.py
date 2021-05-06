n=int(input())
a=list(map(int,input().split()))

swapcount=0

for i in range(n):
    for j in range(n-i-1):
        if(a[j+1]<a[j]):
            t=a[j+1]
            a[j+1]=a[j]
            a[j]=t
            swapcount+=1

print("Frist Element {}".format(a[0]))
print("Last Element {}".format(a[-1]))
print("swapcount : {}".format)(swapcount)
