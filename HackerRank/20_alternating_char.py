def alternatingCharacters(s):
    n=len(s)-1
    res=0
    for i in range(n,-1,-1):
        if(i-1>=0 and s[i-1]==s[i]):
            res+=1
    return res

print(alternatingCharacters(input()))