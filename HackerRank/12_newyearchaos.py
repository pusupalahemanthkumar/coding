t=int(input())

def answer(q,n):
    res=0
    for i in range(n-1,-1,-1):
        if(q[i]!=i+1):
            if(q[i-1]==i+1 and i-1>=0):
                q[i-1]=q[i]
                q[i]=i+1
                res+=1
            elif(q[i-2]==i+1 and i-2>=0):
                q[i-2]=q[i-1]
                q[i-1]=q[i]
                q[i]=i+1
                res+=2
            else:
                print("Too chaotic")
                return
    print(res)


for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    answer(a,n)
   