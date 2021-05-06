import math
def primeFactorization(n):
  d=2
  f,e=[],[]
  while(n>1 and d*d <= n):
    k=0
    while(n%d==0):
      k+=1
      n=n//d
    if(k>=1):
      f.append(d)
      e.append(k)
    d+=1
  if(n>1):
    f.append(n)
    e.append(1)
  print(f,e)
  return e

t=int(input())
for _ in range(t):
    x,y,m=list(map(int,input().split()))
    floor_m=math.gcd(x,y)
    x_factor=x//floor_m
    y_factor=y//floor_m
    res=sum(primeFactorization(x_factor))
    res+=sum(primeFactorization(y_factor))
    print(res,floor_m)


