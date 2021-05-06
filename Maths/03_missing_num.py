a=list(map(int,input().split()))

def MissingNumber(a,n):
    actual_sum=(n*(n+1))//2
    for i in a:
        actual_sum-=i 
    return int(actual_sum)
print(MissingNumber(a,len(a)+1))