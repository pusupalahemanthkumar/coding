n,k=list(map(int,input().split()))

mask=1
i=1
while(i<k):
    mask=mask<<1
    i+=1
if(n & mask):
    print("yes")
else:
    print("no")

