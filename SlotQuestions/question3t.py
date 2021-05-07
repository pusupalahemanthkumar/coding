s=input()
k=int(input())

def maxConsecutive(s,k):
    n=len(s)
    freqCount=[0]*26
    start=0
    end=0
    max_length=0
    maxCount=0

    while(end<n):
        freqCount[ord(s[end])-ord('a')]+=1
        maxCount=max(maxCount,freqCount[ord(s[end])-ord('a')])

        while((end-start-maxCount+1)>k):
            freqCount[ord(s[end])-ord('a')]-=1
            start+=1
        max_length=max(max_length,end-start+1)
        end+=1
    return max
print(maxConsecutive(s,k))
