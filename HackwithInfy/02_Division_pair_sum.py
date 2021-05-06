t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    m=int(input())

     # Hash Map
    remainders={}
    for num in a:
        cur_rem=num%m
        if(cur_rem in remainders):
            remainders[cur_rem]+=1
        else:
            remainders[cur_rem]=1
    num_pairs=0
    for rem in remainders:
        complement=m-rem
        pairs=0
        if(complement==m or (2*complement==m)):
            pairs=(remainders[rem]*(remainders[rem]-1))//2
        elif(complement in remainders):
            pairs=remainders[rem]*remainders[complement]
            remainders[rem]=0
        num_pairs=pairs+num_pairs
    print(num_pairs)





