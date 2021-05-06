from collections import deque
n=int(input())
a=list(map(int,input().split()))

def nextGreater(a):
    n=len(a)
    stack=deque()
    stack.append(0)
    next_greater=[-1]*n
    for i in range(1,n):
        if(len(stack)==0):
            stack.append(i)
            continue
        else:
            while(len(stack)>0 and a[stack[-1]]<a[i]):
                next_greater[stack[-1]]=a[i]
                stack.pop()
        stack.append(i)

    return next_greater
print(nextGreater(a))

