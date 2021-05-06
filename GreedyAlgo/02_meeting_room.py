def comp(a):
    return a[1]
class Solution:
    def maximumMeetings(self,n,start,end):
        n=len(start)
        a=[]
        for i in range(n):
            a.append([start[i],end[i]])
        a=sorted(a,key=comp)
        res=1
        i=0
        for j in range(1,n):
            if(a[j][0]>a[i][1]):
                i=j
                res+=1
        return res
n=int(input())
start=list(map(int,input().split()))
end=list(map(int,input().split()))
print(Solution().activitySelection(n,start,end))