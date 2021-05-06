def comp(a):
    return a[1]
class Solution:
    def minimumPaltforms(self,a,b):
        n=len(arr)
        a.sort()
        b.sort()
        cur_p=res=1
        i=1
        j=0
        while(i<n and j<n):
            if(a[i]<=b[j]):
                cur_p+=1
                i+=1
            elif(a[i]>b[j]):
                cur_p-=1
                j+=1
            res=max(res,cur_p)
        return res
n=int(input())
arr=list(map(int,input().split()))
dep=list(map(int,input().split()))
obj=Solution()
print(obj.minimumPaltforms(arr,dep))

