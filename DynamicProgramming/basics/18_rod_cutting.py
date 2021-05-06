import sys

def cut_Rod(prices,n):
    if(n<=0):
        return 0
    max_val=-sys.maxsize-1

    for i in range(0,n):
        max_val=max(max_val,prices[i]+cut_Rod(prices,n-i-1))
    return max_val

n=int(input())
a=list(map(int,input().split()))
print(cut_Rod(a,n))