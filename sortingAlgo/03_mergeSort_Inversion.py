
def merge(a,temp_a,left,mid,right):
    i=left
    j=mid+1
    k=left 
    inv_count=0
    while(i<=mid and j<=right):
        if(a[i]<a[j]):
            temp_a[k]=a[i]
            i+=1
            k+=1
        else:
            temp_a[k]=a[j]
            inv_count+=(mid-i+1)
            j+=1
            k+=1
    while(i<=mid):
        temp_a[k]=a[i]
        i+=1
        k+=1
    while(j<=right):
        temp_a[k]=a[j]
        j+=1
        k+=1
    for i in range(left,right+1):
        a[i]=temp_a[i]
    return inv_count  
def mergeSort(a,n):
    temp_a=[0]*n 
    return _mergesort(a,temp_a,0,n-1)
def _mergesort(a,temp_a,left,right):
    inv_count=0
    if(left<right):
        mid=(left+right)//2
        inv_count+=_mergesort(a,temp_a,left,mid)
        inv_count+=_mergesort(a,temp_a,mid+1,right)
        inv_count+=merge(a,temp_a,left,mid,right)
    return inv_count

a=list(map(int,input().split()))
n=len(a)
print(mergeSort(a,n))