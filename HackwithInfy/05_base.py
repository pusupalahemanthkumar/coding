# link -  https://prepinsta.com/hackwithinfy/coding/
t=int(input())

for _ in range(t):
    n=int(input())
    res=0
    for i in range(2,n+1):
        num=n 
        base_s=""
        while(num!=0):
            base_s+=str(num%i)
            num=num//i
        print('{} base {}'.format(i,base_s[::-1]))
        base_s=base_s[::-1]
        if(base_s[0]=='1'):
            res+=1
    print(res)



