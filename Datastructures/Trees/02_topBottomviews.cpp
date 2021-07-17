#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node* left;
    struct Node* right;
    Node(int val){
        data=val;
        left=NULL;
        right=NULL;
    }
};

void topView(struct Node* root){
    map<int,int> m;
    queue<pair<Node*,int>> q;
    if(root==NULL){
        return ;
    }
    q.push({root,0});
    while(!q.empty()){
        Node* t=q.front().first;
        int h=q.front().second;
        q.pop();
        if(!m[h]){
            m[h]=t->data;
        }
        if(t->left){
            q.push({t->left,h-1});
        }
        if(t->right){
            q.push({t->right,h+1});
        }
    }
    for(auto x:m){
        cout<<x.second<<" ";
    }
}
void bottomView(struct Node* root){
    map<int,int> m;
    queue<pair<Node*,int>> q;
    if(root==NULL){
        return ;
    }
    q.push({root,0});
    while(!q.empty()){
        Node* t=q.front().first;
        int h=q.front().second;
        q.pop();
       
        m[h]=t->data;
        if(t->left){
            q.push({t->left,h-1});
        }
        if(t->right){
            q.push({t->right,h+1});
        }
    }
    for(auto x:m){
        cout<<x.second<<" ";
    }
}

int main(){
    struct Node* root=new Node(1);
    root->left= new Node(2);
    root->right= new Node(3);
    root->left->left= new Node(4);
    root->left->left->right=new Node(5);
     /*
              1
            /      \
        2               3
      /  \
    4     NULL    NULL      NULL
    / \
 NULL   5


  */
    topView(root);


    return 0;
}