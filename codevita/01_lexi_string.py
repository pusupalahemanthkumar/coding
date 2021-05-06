t=int(input())

for i in range(t):
    p=input()
    s=input()
    for j in p:
        if(j in s):
            print(j,end="")
    print()
