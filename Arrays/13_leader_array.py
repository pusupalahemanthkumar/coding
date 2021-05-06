class Solution:
    def leader(self,a,n):
        res=[a[n-1]]
        for i in range(n-2,-1,-1):
            c=True
            for j in range(i+1,n):
                if(a[i]<a[j]):
                    c=False
                    break
            if(c):
                res.append(a[i])
        print(res)
        return res[::-1]
    def leadersBest(self, a, n):
        #Code here
        res=[a[n-1]]
        max_right=a[n-1]
        for i in range(n-2,-1,-1):
            if(max_right<=a[i]):
                res.append(a[i])
                max_right=a[i]
        return res[::-1]


n=int(input())
a=list(map(int,input().split()))

print(Solution().leader(a,n))


