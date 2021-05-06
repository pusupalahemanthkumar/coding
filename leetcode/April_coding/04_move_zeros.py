# link - https://www.youtube.com/watch?v=PNJoyRaIW7U&list=PLEJXowNB4kPwCPVjDv6KsAsThtDOCQUok&index=4&ab_channel=TECHDOSE

def brute(a,n):
    f=[]
    c=0
    for i in a:
        if(i!=0):
            f.append(i)
        else:
            c+=1
    for i in range(c):
        f.append(0)
    return f
def moveZeros(a,n):
    if(n==0 or n==1):
        return
    left=right=0
    while(right<n):
        if(a[right]==0):
            right+=1
        else:
            a[left],a[right]=a[right],a[left]
            left+=1
            right+=1


n=int(input())
a=list(map(int,input().split()))
print(brute(a,n))
moveZeros(a,n)
print(*a)
