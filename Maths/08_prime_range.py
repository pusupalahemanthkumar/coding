# Prime Range

def primeRange(n,isPrime=[]):
  for i in range(n+1):
    isPrime.append(True)
  isPrime[0]=isPrime[1]=False
  for i in range(2,n//2,1):
    if(isPrime[i]==True):
      for j in range(i*2,n+1,i):
        isPrime[j]=False
  return isPrime


n=int(input())
l=primeRange(n)
for i in range(n+1):
  print(i,l[i])
    