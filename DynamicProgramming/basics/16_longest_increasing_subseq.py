n=int(input())
a=list(map(int,input().split()))
def longest_inc_sub_seq(a,n):
    lis=[1]*(n)
    for i in range(1,n):
        for j in range(0,i):
            if(a[i]>a[j] and lis[i]<lis[j]+1):
                lis[i]=lis[j]+1
    return max(lis)

print(longest_inc_sub_seq(a,n))