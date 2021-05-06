n=int(input())
weights=list(map(int,input().split()))
profits=list(map(int,input().split()))
max_w=int(input())

tab = [[0 for x in range(max_w + 1)] for x in range(n + 1)]

def knapsack(weights,profits,w,n):
    # i ==> items and w = weight(max)
    for i in range(n+1):
        for j in range(w+1):
            if(i==0 or j==0):
                tab[i][j]=0
            elif(weights[i-1]>j):
                tab[i][j]=tab[i-1][j]
            else:
                val2=profits[i-1]+tab[i-1][j-weights[i-1]]
                val1=tab[i-1][j]
                tab[i][j]=max(val1,val2)
    for x in tab:
        print(x)
    return tab[n][w]




print(knapsack(weights,profits,max_w,n))