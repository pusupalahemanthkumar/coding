from functools import cmp_to_key
class Person:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def comparator(a,b):
        if(a.score==b.score):
            if(a.name>b.name):
                return 1
            else:
                return -1
        else:
            return b.score-a.score

n=int(input())
a=[]
for i in range(n):
    name,score=input().split()
    a.append(Person(name,int(score)))
a=sorted(a,key=cmp_to_key(Person.comparator))

for i in range(len(a)):
    print(a[i].name,a[i].score)
