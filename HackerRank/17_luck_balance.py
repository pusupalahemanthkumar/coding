
def comp(a):
    return a[0]
def luckBalance(k, a):
    a_one=[]
    a_zero=[]
    for l,t in a:
        if(t==1):
            a_one.append(l)
        elif(t==0):
            a_zero.append(l)
    a_one=sorted(a_one,reverse=True)
    #print(a_zero,a_one)
  
    return sum(a_zero)+sum(a_one[:k])-sum(a_one[k:])

n,k=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

print(luckBalance(k,a))

