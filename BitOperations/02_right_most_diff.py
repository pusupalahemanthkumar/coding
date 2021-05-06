a,b=list(map(int,input().split()))

def result(a,b):
    mask=counter=1
    while((mask & a)==(mask & b)):
        counter+=1
        mask=mask<<1
    return counter 
print(result(a,b))


