# link - https://www.youtube.com/watch?v=umRBXGTlMb8&ab_channel=ProgrammingSolutions

n=int(input())

def result(n):
    if(n==1):
        return '1'
    if(n==2):
        return '11'
    
    s='11'
    for i in range(2,n):
        new_str=""
        count=1
        for j in range(len(s)):
            if(j==len(s)-1):
                new_str+=str(count)+s[j]
                break
            if(s[j]==s[j+1]):
                count+=1
            else:
                new_str+=str(count)+s[j]
                count=1
        s=new_str
    return s


print(result(n))