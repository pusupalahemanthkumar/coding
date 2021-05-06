import bisect

n=int(input())
a=list(map(float,input().split()))

a=sorted(a,reverse=True)
# min=1.01 pound and max= 3.00 pound
check=[1]*n
res=0
for i in range(n):
    if(check[i]==1):
        complement=3.00-a[i]
        index=-1
        print(a[i],complement)
        for j in range(n-1,i,-1):
            if(a[j]>complement and check[j]==1):
                break
            if(a[j]<=complement and check[j]==1):
                index=j
        if(index!=-1):
            check[i]=0
            check[index]=0
            print("found",str(a[index]))
        else:
            print("Not Found")
        res+=1
print(res)


        


