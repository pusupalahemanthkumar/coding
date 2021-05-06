res=0
def mergeSort(a):
    global res
    if(len(a)>1):
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        mergeSort(l)
        mergeSort(r)
        i=j=k=0
        while(i<len(l) and j<len(r)):
            if(l[i]<=r[j]):
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
                res+=len(l[i:])
            k+=1
        while(i<len(l)):
            a[k]=l[i]
            k+=1
            i+=1
        while(j<len(l)):
            a[k]=r[j]
            j+=1
            k+=1


# Input
n=int(input())
a=list(map(int,input().split()))

print(a)
mergeSort(a)
print(a)
print(res)