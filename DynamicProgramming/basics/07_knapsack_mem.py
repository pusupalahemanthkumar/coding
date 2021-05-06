n=int(input())
weights=list(map(int,input().split()))
profits=list(map(int,input().split()))
max_w=int(input())

mem= [[-1 for i in range(max_w+1)] for j in range(n + 1)]

def knapsack(weights,profits,w,n):
    #base Condition
    if(n==0 or w==0):
        return 0
    if(mem[n][w]!=-1):
        return mem[n][w]
    if(weights[n]>w):
        mem[n][w]=knapsack(weights,profits,w,n-1)
        return mem[n][w]
    else:
        val1=knapsack(weights,profits,w,n-1)
        val2=(profits[n]+knapsack(weights,profits,w-weights[n],n-1))
        mem[n][w]=max(val1,val2)
        return mem[n][w]

print(knapsack(weights,profits,max_w,n-1))