#  MathematicalFundamentals- FastExpo 
def power(a,n):
  if(a==0): # 0^n =1
    return 0
  if(n==0): # a^0 =1
    return 1
  r=power(a,n//2)
  if(n & 1):
    return r*a*r
  else:
    return r*r

a,n=list(map(int,input().split()))
print(power(a,n))