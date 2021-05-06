# Tabulation (Bottom Up)

def fibo(n):
    f=[0]*(n)
    f[1]=1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]

n=int(input())-1
print(fibo(n))
