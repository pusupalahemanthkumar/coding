# Prime Factorization
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
  return f,e
  
n=int(input())
print(primeFactorization(n))
