n=int(input())
prices=list(map(int,input().split()))
length=list(map(int,input().split()))
maxlen=int(input())

mem=[[0 for _ in range(maxlen+1)] for __ in range(n+1)]
def ubk(prices,length,maxlen,n):
    if(n==0 or maxlen==0):
        return 0
    if(length[n-1]>maxlen):
        mem[n][maxlen]=ubk(prices,length,maxlen,n-1)
    else:
        mem[n][maxlen]=max(ubk(prices,length,maxlen,n-1),prices[n-1]+ubk(prices,length,maxlen-length[n-1],n))
    return mem[n][maxlen]

print(ubk(prices,length,maxlen,n))