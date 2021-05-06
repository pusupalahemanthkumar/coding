# Memoization (Top Down)
def fibo(n,lookup):
    if(n==0 or n==1):
        lookup[n]= n 
    if(lookup[n] is None):
        lookup[n]=fibo(n-1,lookup)+fibo(n-2,lookup)
    
    return lookup[n]

n=int(input())
lookup=[None]*(n)
print(fibo(n-1,lookup))