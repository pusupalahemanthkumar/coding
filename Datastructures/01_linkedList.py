class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def append(self,data):
        newNode=Node(data)

        if self.head==None:
            self.head=newNode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newNode
    def display(self):
        t=self.head
        while(t.next):
            print("{}->".format(t.data),end="")
            t=t.next
        print(t.data)
        
n=int(input())
a=LinkedList()
for i in range(n):
    a.append(int(input()))
a.display()









