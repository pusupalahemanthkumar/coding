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
void leftView(struct Node* root){
    vector<int> ans;
    queue<Node* > q;
    if(!root){
        return ;
    }
    q.push(root);
    while(!q.empty()){
        int sz=q.size();
        ans.push_back(q.front()->data);
        while(sz--){
            Node* t=q.front();
            q.pop();
            if(t->left){
                q.push(t->left);
            }
            if(t->right){
                q.push(t->right);
            }
        }
    }
    for(auto x: ans){
        cout<<x<<" ";
    }
    cout<<endl;


}
void rightView(struct Node* root){
    vector<int> ans;
    queue<Node* > q;
    if(!root){
        return ;
    }
    q.push(root);
    while(!q.empty()){
        int sz=q.size();
        Node* t;
        while(sz--){
            t=q.front();
            q.pop();
            if(t->left){
                q.push(t->left);
            }
            if(t->right){
                q.push(t->right);
            }
        }
        cout<<t->data<<" ";
    }
    cout<<endl;

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
 


    return 0;
}