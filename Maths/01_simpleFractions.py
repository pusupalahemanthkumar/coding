n,d=list(map(int,input().split()))

def simpleFraction(n,d):
    ans=""
    q=n//d 
    r=n%d 
    ans+=str(q)
    if(r==0):
        return ans
    else:
        ans+="."
        freq={}
        while(r!=0):
            if(freq.get(r)):
                l=freq[r]
                ans=ans[:l]+"("+ans[l:]+")"
                break
            else:
                freq[r]=len(ans)
                r*=10
                q=r//d
                r=r%d 
                ans+=str(q)
    return ans
print(simpleFraction(n,d))

