#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
};

void printList(Node* n){
    while(n!=NULL){
        cout<< n->data<<" ";
        n=n->next;
    }
}
void push(Node** head_ref,int new_data){
    Node* new_node=new Node();

    new_node->data=new_data;

    new_node->next=(*head_ref);
    *head_ref=new_node;
}

void append(Node** head_ref,int new_data){

    Node* new_node =new Node();

    new_node->data=new_data;
    new_node->next=NULL;
     
     Node* cur_node=*head_ref;

    //  If Linkedlist is empty
     if(cur_node==NULL){
         *head_ref=new_node;
         return;
     }

     while(cur_node->next!=NULL){
         cur_node=cur_node->next;
     }
     cur_node->next=new_node;
     return;
}
void insertAfter(Node** head_ref,int prevData,int new_data){
    if(head_ref==NULL){
        return;
    }
    Node* new_node= new Node();
    new_node->data= new_data;
    
    Node* cur_node= *head_ref;
    while(cur_node->next !=NULL && cur_node->data!=prevData){
        cur_node=cur_node->next;
    }
    new_node->next=cur_node->next;
    cur_node->next=new_node;
}
int getMiddle(Node* head){
    int len=0;
    Node* temp=head;
    Node* t=head;
    while(temp!=NULL){
        temp=temp->next;
        len++;
    }
    if(len==0){
        return -1;
    }
    int i=0;
    while(i<(len/2)){
        t=t->next;
        i++;
    }
    return t->data;
}

Node* reverse(Node* head){
    Node* prev=NULL;
    Node* next=NULL;
    Node* cur=head;
    while(cur!=NULL){
        next=cur->next;
        cur->next=prev;
        prev=cur;
        cur=next;
    }
    return prev;
}

int getMiddleBest(Node *head)
{
       struct Node *slow_ptr = head;
        struct Node *fast_ptr = head;
  
        if (head!=NULL)
        {
            while (fast_ptr != NULL && fast_ptr->next != NULL)
            {
                fast_ptr = fast_ptr->next->next;
                slow_ptr = slow_ptr->next;
            }
            return slow_ptr->data;
        }
        return -1;
    
}

int main(){

    Node* head = NULL;
    append(&head,1);
    append(&head,2);
    append(&head,3);
    append(&head,4);
    push(&head,5);
    insertAfter(&head,3,99);
    insertAfter(&head,4,99);
    printList(head);
    
    cout<<"\n"<<getMiddleBest(head)<<endl;
    head=reverse(head);
    printList(head);
    
  

    return 0;
}