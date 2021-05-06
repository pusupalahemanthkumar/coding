t=int(input())

for i in range(t):
    n=int(input())
    # Edge Case
    if(n==1):
        print("No")
        continue

    i=2
    res={1}
    while(i*i<=n):
        if(n%i==0):
            res.add(i)
            res.add(n//i)
        i+=1
    print(res)
    divisor_sum=sum(res)
    if(divisor_sum==n):
        print("Yes")
    else:
        print("No")
 


