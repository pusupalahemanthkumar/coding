/*
Check Cyclic DFS

*/
#include<bits/stdc++.h>
using namespace std;

bool checkForCycle(int node,int parent,vector<int> adj[],vector<int> &vis){
   vis[node]=1;
   for(auto it:adj[node]){
       if(!vis[it]){
           if(checkForCycle(it,node,adj,vis)){
               return true;
           }
       }else if(it!=parent){
               return true;
        }
   }

    return false;

}

bool isCycle(int V, vector<int> adj[]){
    vector<int> vis(V,0);
    for(int i=0;i<V;i++){
        if(!vis[i]){
            if(checkForCycle(i,-1,adj,vis)){
                return true;
            }
        }
    }
    return false;
}

int main(){
    int V,E;
    cin>>V>>E;
    vector<int> adj[V+1];
    for(int i=0;i<E;i++){
        int u,v;
        cin>>u>>v;
        adj[u].push_back[v];
        adj[v].push_back[u];
    }
    if(isCycle(V,adj)){
        cout<<"1"<<endl;
    }else{
        cout<<"0"<<endl;
    }
    return 0;
}