n=int(input())

def result(n):
    counter=1
    mask=1
    while(n):
        if(n & mask):
            return counter
        n=n>>1
        counter+=1
print(result(n))
    
    