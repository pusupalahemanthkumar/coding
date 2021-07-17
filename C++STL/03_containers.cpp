#include<bits/stdc++.h>
using namespace std;

array<int,100> ga; // Default value is zero

int main(){
    int d[5]={0}; // [0,0,0,0,0]

    array<int,100> a; // Default Value is garbage

    array<int,5> b={1,5,6}; // [1 5 6 0 0]
    array<int,5> c={0}; // [0,0,0,0,0]

    array<int,5> e;
    e.fill(5); // [5,5,5,5,5]

    // e.at(index);
    for(int i=0;i<5;i++){
        cout<<e.at(i)<<" ";
    }
    cout<<endl;

    // Iterators
    // begin() end() rbegin() rend() 
    array<int,5> f={1,2,3,4,5};
    for(auto it=f.begin();it!=f.end();it++){
        cout<<*it<<" ";
    }
    cout<<endl;

    for(auto it=f.rbegin();it!=f.rend();it++){
        cout<<*it<<" ";
    }
    cout<<endl;

    for(auto it:f){
        cout<<it<<" ";
    }
    cout<<endl;

    cout<<f.size()<<endl;
    cout<<endl;
    
    string str="hemanth";
    for(auto it:str){
        cout<<it<<" ";
    }
    cout<<endl;


    cout<<str.size()<<endl;

}