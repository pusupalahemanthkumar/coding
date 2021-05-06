# link - https://www.youtube.com/watch?v=C8UjlJZsHBw&ab_channel=TECHDOSE

class Solution:
    def trappingWater(self, a,n):
        #Code here
        left=[0]*n
        right=[0]*n
        res=0
        left[0]=a[0]
        for i in range(1,n):
            left[i]=max(left[i-1],a[i])
        right[n-1]=a[n-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],a[i])
        for i in range(0,n):
            res+=min(left[i],right[i])-a[i]
        return res
n=int(input())
a=list(map(int,input().split()))
print(Solution().trappingWater(a,n))