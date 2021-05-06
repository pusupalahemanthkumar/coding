n=int(input())
a=list(map(int,input().split()))

actual_s=(n*(n+1))/2

for i in a:
    actual_s-=i
print(int(actual_s))