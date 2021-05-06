
# mask & n ==> 1 means bit is set
# mask & n ==> 0 means bit is not set
# 
n,l,r=list(map(int,input().split()))
val=power=0
mask=i=1
# Include all right most bits
while(i<l):
    if(mask &n):
        val+=2**power
    mask=mask<<1
    power+=1
    i+=1
while(i<=r):
    if(not(mask & n)):
        val+=2**power
    power+=1
    i+=1
    mask=mask<<1
while(i<=10):
    if(mask &n):
        val+=2**power
    mask=mask<<1
    power+=1
    i+=1
print(val)


