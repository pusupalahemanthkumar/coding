n=int(input())
result=0
i=0
while(n):
    if(n&1==0):
        result+=(1<<i)
    i+=1
    n=n>>1
print(result)