m,n=list(map(int,input().split()))
count=0
while(m!=n):
    m=m>>1
    n=n>>1
    count+=1
print(m<<count)