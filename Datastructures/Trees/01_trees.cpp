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
void printPostOrder(struct Node* node){
  if(node==NULL){
    return ;
  }
  printPostOrder(node->left);
  printPostOrder(node->right);
  cout<<node->data<<" ";
}
void printInorder(struct Node* node)
{
    if (node == NULL)
        return;
    printInorder(node->left);
    cout << node->data << " ";
    printInorder(node->right);
}

void printPreorder(struct Node* node)
{
    if (node == NULL)
        return;
    cout << node->data << " ";
    printPreorder(node->left);
    printPreorder(node->right);
}

// Level Order (BFS)
void printLevelOrder(Node *root)
{
    // Base Case
    if (root == NULL)  return;
 
    // Create an empty queue for level order traversal
    queue<Node *> q;
 
    // Enqueue Root and initialize height
    q.push(root);
 
    while (q.empty() == false)
    {
        // Print front of queue and remove it from queue
        Node *node = q.front();
        cout << node->data << " ";
        q.pop();
 
        /* Enqueue left child */
        if (node->left != NULL)
            q.push(node->left);
 
        /*Enqueue right child */
        if (node->right != NULL)
            q.push(node->right);
    }
}


int main(){
    struct Node* root=new Node(1);
    root->left= new Node(2);
    root->right= new Node(3);
    root->left->left= new Node(4);
    /*
              1
            /      \
        2               3
      /  \
    4     NULL    NULL      NULL
    / \
 NULL   NULL


  */
  printPreorder(root);
  cout<<endl;
  printInorder(root);
  cout<<endl;
  printPostOrder(root);
  cout<<endl;
  printLevelOrder(root);


 return 0;

}