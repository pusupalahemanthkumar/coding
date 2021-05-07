s=input()
n=int(input())
p=[]
for i in s:
    p.append(i)
p=set(p)
p=list(p)
maxn=[]
count=1
for i in range(len(p)):
    for j in range(len(s)):
        st=s[:j]
        e=s[j+n:]
        c=p[i]*n
        k=st+c+e
        final=k[:len(s)]
        count=1
        d = { r:1 for r in final}
        for r in range(len(final)-1):
            if final[r] == final[r+1]:
                d[final[r]] += 1
        keymax = max(d, key=d.get)
        maxn.append(d[keymax])
print(max(maxn))