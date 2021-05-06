n=int(input())
a=list(map(int,input().split()))

i=res=0
while(i<n):
    if(a[i]==0):
        if(i+2<n and a[i+2]==0):
            i+=2
        else:
            i+=1
        res+=1
print(res-1)