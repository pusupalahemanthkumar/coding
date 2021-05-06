from collections import deque
s=input()

def isBalanced(s):
    n=len(s)
    stack=deque()
    for i in s:
        if(i=="[" or i=="{" or i=="("):
            stack.append(i)
            print(stack,i)
        elif(i=="]" or i=="}" or i==")"):
            top=stack.pop()
            print(stack,i,top)
            if(i=="]" and top!='['):
                print("test1")
                return False   
            elif(i==')' and top!='('):
                print("test2")
                return False
            elif(i=='}' and top!='{'):
                print("test3")
                return False
            
    return True if len(stack)==0 else False

print(isBalanced(s))
