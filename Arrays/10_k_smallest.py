import heapq
class Solution:
    def kthSmallest(self,a,k):
        n=len(a)
        heapq.heapify(a)
        for i in range(1,k):
            heapq.heappop(a)
        return heapq.heappop(a)

a=list(map(int,input().split()))
k=int(input())

print(Solution().kthSmallest(a,k))