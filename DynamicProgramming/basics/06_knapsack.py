def knapsack(weights,profits,w,n):
    if(w==0 or n==0):
        return 0
    if(weights[n]>w):
        return knapsack(weights,profits,w,n-1)
    else:
        return max(knapsack(weights,profits,w,n-1),profits[n]+knapsack(weights,profits,w-weights[n],n-1))


n=int(input())
weights=list(map(int,input().split()))
profits=list(map(int,input().split()))
max_w=int(input())

print(knapsack(weights,profits,max_w,n-1))
