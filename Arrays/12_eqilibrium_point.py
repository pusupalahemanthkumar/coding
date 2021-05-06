class Solution:
    def equilibriumPoint(self,a, n):
        # Your code here
        t_sum=sum(a)
        l_sum=0
        for i in range(n):
            t_sum-=a[i]
            if(l_sum==t_sum):
                return i+1
            l_sum+=a[i]
        return -1



n=int(input())
a=list(map(int,input().split()))
print(Solution().equilibriumPoint(a,n))