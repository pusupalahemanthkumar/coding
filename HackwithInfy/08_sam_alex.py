import bisect

n=int(input())
a=list(map(int,input().split()))
k=int(input())
count=0
for i in range(n):
    div=a[i]//k
    count+=div
    if(a[i]%k!=0):
        count+=1
if(count%2==0):
    print("Alex")
else:
    print("sam")

