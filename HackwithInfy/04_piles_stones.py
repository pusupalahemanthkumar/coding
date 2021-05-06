# link -  https://prepinsta.com/hackwithinfy/coding/

t=int(input())

for _ in range(t):
    a,b,c,x,y=list(map(int,input().split()))
    if((a+b+c)!=(x+y)):
        print("No")
    else:
        if(y<min(a,min(b,c)) or x<min(a,min(b,c))):
            print("No")
        else:
            print("Yes")
            
