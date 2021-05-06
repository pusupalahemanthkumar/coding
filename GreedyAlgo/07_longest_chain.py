class Pair:
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
def comp(x):
    return x.a 
def result(p,n):
    p=sorted(p,key=comp)
    for i in range(n):
        print(p[i].a,p[i].b,end=" ")
    res=1
    i=0
    print()
    for j in range(1,n):
        if(p[j].a>p[i].b):
            i=j
            res+=1
    return res


n=int(input())
p=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    p.append(Pair(a,b))

print(result(p,n))

