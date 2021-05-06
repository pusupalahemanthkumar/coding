class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        a.sort()
        b.sort(reverse=True)
        res=a[0]*b[0]
        for i in range(1,n):
            res+=a[i]*b[i]
        return res
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(Solution().minValue(a,b,n))