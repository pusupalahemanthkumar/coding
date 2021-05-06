n=int(input())

def nthNaturalNumber(n):
    base=9
    ans=""
    while(n>0):
        r=n%base
        n=n//base
        ans+=str(r)
    return ans[::-1]
print(nthNaturalNumber(n))
