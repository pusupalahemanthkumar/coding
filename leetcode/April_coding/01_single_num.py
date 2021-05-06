# link - https://www.youtube.com/watch?v=krgK0UlfNYY&list=PLEJXowNB4kPwCPVjDv6KsAsThtDOCQUok&index=1&ab_channel=TECHDOSE
def single_num(a,n):
    xor=0
    for i in a:
        xor^=i
    return xor

n=int(input())
a=list(map(int,input().split()))
print(single_num(a,n))
