# link - https://www.youtube.com/watch?v=HddgLcq9Efs&list=PLEJXowNB4kPxBwaXtRO1qFLpCzF75DYrS&index=17&ab_channel=TECHDOSE

n,x=list(map(int,input().split()))
a=list(map(int,input().split()))
mem={}
def minOperations(a,x,left,right,count):
    if(x==0):
        return count 
    if(x<0 or left>right):
        return 1e6
    key="{}*{}*{}".format(left,right,x)
    if(mem.get(key)):
        return mem[key]
    l=minOperations(a,x-a[left],left+1,right,count+1)
    r=minOperations(a,x-a[right],left,right-1,count+1)
    mem[key]=min(l,r)
    return mem[key] if mem[key]<1e6 else -1


print(minOperations(a,x,0,n-1,0))