n=int(input())
a=list(map(int,input().split()))

cur_max=a[0]
end_max=0
start=end=s=0

for i in range(n):
    end_max+=a[i]
    if(cur_max<end_max):
        cur_max=end_max
        start=s
        end=i
    if(end_max<0):
        s=i+1
        end_max=0
print(start,end,cur_max)