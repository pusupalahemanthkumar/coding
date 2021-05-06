n,s=list(map(int,input().split()))
a=list(map(int,input().split()))

def subArraySum(a,n,s):
    cur_sum=a[0]
    start=0
    i=1
    while(i<=n):
        while(cur_sum>s and start<i-1):
            cur_sum-=a[start]
            start+=1
        
        if(cur_sum==s):
            print("Found")
            return [start,i-1]
        
        if(i<n):
            cur_sum+=a[i]
        i+=1
    print("Not found")
    return [-1]

res=subArraySum(a,n,s)
for i in res:
    print(i,end=" ")


        


