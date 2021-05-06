a=list(map(int,input().split()))
k=int(input())

a.sort()
res=curp=0

for i in a:
    if(curp+i<=k):
        res+=1
        curp+=i
    else:
        break
print(res)
