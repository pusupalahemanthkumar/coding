# Useful Resource- https://wiki.python.org/moin/TimeComplexity

# Input
a=list(map(int,input().split()))
k=int(input())

# Hash Map
d=dict.fromkeys(set(a),0)
for i in a:
    d[i]+=1
count=0
res=[]
for i in a:
    complement=k-i
    if(d.get(complement)):
        count+=1
        res.append([i,complement])
print(count//2,res)


