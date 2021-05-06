n=int(input())
coins=list(map(int,input().split()))
amount=int(input())

def count_coins(coins,n,amount):
    dp=[[0 for _ in range(amount+1)] for __ in range(n+1)]
    dp[0][0]=1
    for i in range(1,amount+1):
        dp[0][i]=0
    for i in range(1,n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,amount+1):
            if(j<coins[i-1]):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-coins[i-1]]+dp[i-1][j]
    for x in dp:
        print(x)
    return dp[n][amount]
    

print(count_coins(coins,n,amount))