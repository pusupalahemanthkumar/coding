class Solution:
    def getMin(self,a,n,k):
        # n==1 only one Element
        if(n==1):
            return 0
        a.sort()
        ans=a[n-1]-a[0]
        small=a[0]+k
        big=a[n-1]-k
        if(small>big):
            small,big=big,small
        
        for i in range(1,n-1):
            subtract=a[i]-k
            add=a[i]+k

            if(subtract>=small or add<=big):
                

        

        
       

n,k=list(map(int,input().split()))
a=list(map(int,input().split()))

print(Solution().getMin(a,n,k))
