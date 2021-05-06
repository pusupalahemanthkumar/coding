s=input()
def isValid(s):
    n=len(s)
    f=dict.fromkeys(set(a),0)
    for i in s:
        f[i]+=1
    count_2=0
    for k,v in f.items():
        if(count_2>=2):
            return False
        if(v==2):
            count_2+=1
        
print("Yes" if isValid(s) else "No")
