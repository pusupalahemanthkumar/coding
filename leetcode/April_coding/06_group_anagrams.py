s=list(input().split())
n=len(s)

first="".join(sorted(s[0]))
d={first:[s[0]]}

print(d)
for i in range(1,n):
    t="".join(sorted(s[i]))
    if(t in d.keys()):
        d.get(t).append(s[i])
    else:
        d[t]=[s[i]]
print(d)



