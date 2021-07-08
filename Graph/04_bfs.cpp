/*
BFS( Breadth First Search)


*/
#include<bits/stdc++.h>
using namespace std;


void bfs_traversal(vector<int> adj[],int V,vector<int> &res){
    vector<int> vis(V,0);
    
    queue<int> q;
    // Pushing Starting Vertex (Node 0)
    q.push(0);
    vis[0]=1;
    
    while(!q.empty()){
        // Adding Node to Output
        int node=q.front();
        q.pop();
        res.push_back(node);
        // Adding Adjacent Nodes To Queue
        for(auto it :adj[node]){
            if(!vis[it]){
                q.push(it);
                vis[it]=1;
            }
        }
    }
}

int main(){
    int V,E;
    cin>>V>>E;
    vector<int> adj[V];
    for(int i=0;i<E;i++){
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> res;
    bfs_traversal(adj,V,res);
    for(int i=0;i<V;i++){
        cout<<res[i]<<" ";
    }
}
