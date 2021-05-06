n=int(input())
coins=list(map(int,input().split()))
amount=int(input())

def coin_change(coins,n,amount):
    dp=[[0 for i in range(amount+1) ] for j in range(n+1)]
    for i in range(n+1):
        for j in range(amount+1):
            if(i==0 and j==0):
                dp[i][j]=0
            elif(j==0):
                dp[i][j]=0
            elif(i==0):
                dp[i][j]=1e5
            elif(coins[i-1]>j):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
    for x in dp:
        print(x)

    return -1 if dp[n][amount]>1e4 else dp[n][amount]
print(coin_change(coins,n,amount))
