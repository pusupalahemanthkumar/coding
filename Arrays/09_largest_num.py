import functools  

def mycmp(a, b):
    num1=int(str(a)+str(b))
    num2=int(str(b)+str(a))
    if num1 > num2:
        return -1
    elif num1 < num2:
        return 1
    else:
        return 0

a=list(map(int,input().split()))
a=sorted(a,key=functools.cmp_to_key(mycmp))

print("".join([str(i) for i in a]))
