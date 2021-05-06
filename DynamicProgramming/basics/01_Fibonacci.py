def fibo(n):
    if(n<=1):
        return n
    return fibo(n-1)+fibo(n-2)

# Fibonacci Numbers : 0 1 1 2 3 5 8 13 
# Time Complexity : 2^n

n=int(input())-1
print(fibo(n))