def primeRange(n):
    prime_nums=[]
    prime_c=[1]*(n)
    prime_c[0]=prime_c[1]=0
    for i in range(2,(n//2)+1):
        if(prime_c[i]):
            for j in range(i*2,n,i):
                prime_c[j]=0
    for i in range(len(prime_c)):
        if(prime_c[i]):
            prime_nums.append(i)
    return prime_nums


n=int(input())
res=0
a=primeRange(n)
size=len(a)
for i in range(2,size):
    s=0
    for j in range(0,i):
        s+=a[j]
        if(s==a[i]):
            res+=1
            break
        if(s>a[i]):
            break
print(res)




