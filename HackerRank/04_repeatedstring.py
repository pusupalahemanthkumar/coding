s=input()
n=int(input())

slen=len(s)
res=s.count('a')*(n//slen)

for i in range(n%slen):
    if(s[i]=='a'):
        res+=1
print(res)