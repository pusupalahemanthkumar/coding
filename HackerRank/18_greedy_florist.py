
def getMinimumCost(k, c):
    c=sorted(c,reverse=True)
    res=0
    for i in range(len(c)):
        res+=((i//k)+1)*c[i]
    return res
    
n,k=list(map(int,input().split()))
a=list(map(int,input().split()))

print(getMinimumCost(k,a))