# Link - https://prepinsta.com/hackwithinfy/coding/
# Input 
t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    freq=dict.fromkeys(set(a),0)
    i=0
    while(i<n):
        freq[a[i]]+=1
        if(i+1<n and a[i]==a[i+1]):
            i+=2
        else:
            i+=1
    print(freq)
    mav=max(freq.values())
    item=90000
    for k,v in freq.items():
        if(item>k and v==mav):
            item=k
    print(item)


    


