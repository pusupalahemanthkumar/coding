class Solution:
    def toyCount(self, n, k, a):
        # code here
        a.sort()
        res=0
        cur_p=0
        for i in range(n):
            cur_p+=a[i]
            if(cur_p>k):
                break
            elif(cur_p<k):
                res+=1
            else:
                res+=1
                break
        return res

n=int(input())
k=int(input())
a=list(map(int,input().split()))
print(Solution().toyCount(n,k,a))
