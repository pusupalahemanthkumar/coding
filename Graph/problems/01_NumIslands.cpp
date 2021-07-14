/*
BFS Approach
*/
#include<bits/stdc++.h>
using namespace std;

 void bfs(vector<int> &matrix[],int x,int y,int r,int c)
    {
        if(x<0 || x>=r || y<0 || y>=c || matrix[x][y]!='1')  //Boundary case for matrix
            return;
        
        //Mark current cell as visited
        matrix[x][y] = '2';
        
        //Make recursive call in all 4 adjacent directions
        bfs(matrix,x+1,y,r,c);  //DOWN
        bfs(matrix,x,y+1,r,c);  //RIGHT
        bfs(matrix,x-1,y,r,c);  //TOP
        bfs(matrix,x,y-1,r,c);  //LEFT
    }

int numIslands(vector<int> grid[]){
    int rows=grid.size();
    if(rows==0){
        return 0;
    }
    int cols=grid[0].size();

    int res=0;
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            if(grid[i][j]==1){
                bfs(grid,i,j,rows,cols);
                res+=1
            }
        }
    }
}

int main(){
    int r,c;
    cin>>r>>c;
    vector<int> grid[c];
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin>>grid[i][j];
        }
    }
    cout<<numIslands(gird)<<endl;

}