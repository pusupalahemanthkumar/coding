def makeAnagram(a,b):
    buffer=[0]*26
    for char in a:
        buffer[ord(char)-ord('a')]+=1
    for char in b:
        buffer[ord(char)-ord('a')]-=1
    return sum(map(abs,buffer))
s1=input()
s2=input()
print(makeAnagram(s1,s2))