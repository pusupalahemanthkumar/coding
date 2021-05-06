# i => prev
# j => next
# num => cur
def isPeak(a,n,num,i,j):
    if(i>=0 and a[i]>num):
        return False
    if(j<n and a[j]>num):
        return False
    return True
def isTrough(a,n,num,i,j):
    if(i>=0 and a[i]<num):
        return False
    if(j<n and a[j]<num):
        return False
    return True
def result(a,n):
    res=0
    p=[]
    t=[]
    for i in range(n):
        if(isPeak(a,n,a[i],i-1,i+1)):
            p.append(i)
            print("peak",end=" ")
        if(isTrough(a,n,a[i],i-1,i+1)):
            t.append(i)
            print("tr",end=" ")
        print(i,p,t)
        if(len(p)==2):
            res=max(res,abs(p[0]-p[1]))
            del p[0]
        if(len(t)==2):
            res=max(res,abs(t[0]-t[1]))
            del t[0]
    return res
n=int(input())
a=list(map(int,input().split()))
print(result(a,n))
        

