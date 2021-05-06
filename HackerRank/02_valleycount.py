n=int(input())
a=input()

valleyCount=level=0

for i in a:
    if(i=='D'):
        level-=1
    if(i=='U'):
        level+=1
    if(level==0 and i=='U'):
        valleyCount+=1
print(valleyCount)
