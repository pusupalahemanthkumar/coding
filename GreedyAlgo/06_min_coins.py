# link - https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/

deno=[1,2,5,10,20,50,100,500,1000]

def result(n):
    i=len(deno)-1
    res=0
    while(i>=0):
        while(n>=deno[i]):
            n-=deno[i]
            res+=1
        i-=1
    return res


num=int(input())
print(result(num))