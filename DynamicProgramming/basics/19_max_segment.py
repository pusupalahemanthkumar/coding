import sys
n=int(input())
x,y,z=list(map(int,input().split()))
dp=[-1]*(n+1)
class Solution:
    def maximizeTheCuts(self,n,x,y,z):
        if(n==0):
            return 0
        if(dp[n]!=-1):
            return dp[n]
        op1=op2=op3=-sys.maxsize-1
        if(n>=x):
            op1=self.maximizeTheCuts(n-x,x,y,z)
        if(n>=y):
            op2=self.maximizeTheCuts(n-y,x,y,z)
        if(n>=z):
            op3=self.maximizeTheCuts(n-z,x,y,z)
        dp[n]=1+max(op1,max(op2,op3))
        return dp[n] if dp[n]!=-1 else 0

print(Solution().maximizeTheCuts(n,x,y,z))

