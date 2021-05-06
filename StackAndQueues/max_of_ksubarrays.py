import bisect
n=int(input())
a=list(map(int,input().split()))
k=int(input())


class Solution:
    def max_of_subarrays(self,a,n,k):
        res=[]
        cur_win=sorted(a[:k])
        res.append(cur_win[-1])
        for i in range(k,n-k+1):
            del cur_win[bisect.bisect_left(curw,a[i-d])
            bisect.insort(cur_win,a[i])
            res.append(cur_win[-1])
        return res
print(*Solution().max_of_subarrays(a,n,k))
