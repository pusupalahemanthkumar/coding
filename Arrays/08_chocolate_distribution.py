class Solution:
    def getMinDiff(self,a,n,m):
        if(m==0 or n==0):
            return 0
        if(n<m):
            return -1
        a.sort()

        res=a[m-1]-a[0] # First window
        #print(res)

        for i in range(m,n):
            cur_res=a[i]-a[i-m+1]
            res=min(res,cur_res)
            #print(i,cur_res,res)
        return res

n=int(input())
a=list(map(int,input().split()))
m=int(input())

obj=Solution()
print(obj.getMinDiff(a,n,m))
