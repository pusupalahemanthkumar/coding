# link - https://www.youtube.com/watch?v=GmHengYK3Nk&list=PLEJXowNB4kPwCPVjDv6KsAsThtDOCQUok&index=7&ab_channel=TECHDOSE

# METHOD -2 HASH MAP


a=list(map(int,input().split()))
a.sort()
left=0
right=1
c=0
n=len(a)
while(right<n):
    if(a[right]==1+a[left]):
        c+=(right-left)
        left=right
        right+=1
    elif(a[right]==a[left]):
        right+=1
    else:
        left=right
        right+=1
print(c)