#

# Taking Input
n=int(input())
a=list(map(int,input().split()))

# Hash Map
f=dict.fromkeys(set(a),0)
for i in a:
    f[i]+=1

res=0 
for k,v in f.items():
    res+=v//2
print(res)