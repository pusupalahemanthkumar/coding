/*
Check Cyclic BFS

*/
#include<bits/stdc++.h>
using namespace std;

bool checkForCycle(int s,int V,vector<int> adj[],vector<int> &vis){
    queue<pair<int,int>> q;
    vis[s]=1;
    q.push({s,-1});

    while(!q.empty()){
        int node= q.front().first;
        int parent=q.front().second;
        q.pop();
        for(auto it : adj[node]){
            if(!vis[it]){
                vis[it]=1;
                q.push({it,node});
            }else if(parent!=it){
                return true;
            }
        }

    }
    return false;

}

bool isCycle(int V, vector<int> adj[]){
    vector<int> vis(V,0);
    for(int i=0;i<V;i++){
        if(!vis[i]){
            if(checkForCycle(i,V,adj,vis)){
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