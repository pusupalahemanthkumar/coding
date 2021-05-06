
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

def comp(x):
    return x.a
def maxChainLen(P, n):
    # Parr:  list of pair
    #code here
    P=sorted(P,key=comp)
    lis=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if(P[i].a>P[j].b and lis[i]<lis[j]+1):
                lis[i]=lis[j]+1
    return max(lis)

n=int(input())
p=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    p.append(Pair(a,b))

print(maxChainLen(p,n))