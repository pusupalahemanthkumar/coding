s=input()
k=int(input())

def maxConsecutive(s,k):
    n=len(s)
    counta=0
    lena=0
    max_lena=0
    for i in range(n):
        if(s[i]=='b' or s[i]=='c'):
            counta+=1
        while(counta>k):
            if(s[i]=='b' or s[i]=='c'):
                counta-=1
            lena+=1
    max_lena=max(max_lena,i-lena+1)
    return max_lena
    
print(maxConsecutive(s,k))

