import sys
n=int(input())
a=list(map(int,input().split()))

def kandanesAlgo(a):
    n=len(a)
    msf=-sys.maxsize-1
    men=0
    for i in range(n):
        men+=a[i]
        if(men<a[i]):
            men=a[i]
        if(msf<men):
            msf=men
    return msf 
print(kandanesAlgo(a))