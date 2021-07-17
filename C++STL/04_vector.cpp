#include<bits/stdc++.h>
using namespace std;

// bool a[100000000];// For bool => max size 10^8
// int a[1000000]; //  For int , double , cha rmax size 10^7
int main(){
    // For int , double , char
    // int a[1000000]; // max size 10^6
 
    // For bool => max size 10^7
    // bool a[10000000];


    vector<int> a; // size of zero is created
    cout<<a.size()<<endl;
    a.push_back(1);
    a.push_back(2);
    a.emplace_back(1); // Faster than push_back
    cout<<a.size()<<endl;
    a.pop_back(); // {1}
    cout<<a.size()<<endl;

    // a.clear(); // erase all elements at once

    vector<int> vect1(4,0); // {0,0,0,0}
    vector<int> vect2(4,10); // {10,10,10,10}

    // Copy
    vector<int> vect3(vect2.begin(),vect2.end());
    // vector<int> vect3(vect2.begin(),vect2.begin()+2); // Copy first two elements
    vector<int> vect3(vect2);

    // lower bound , upper bound
    // swap swap(v1,v2)

    // To define 2d vector
    vector<vector<int>> vec;


    for(auto it : vec){
        for(auto it1 :it){
            cout<<it1<<" ";
        }
        cout<<endl;
    }
    for(int i=0;i<vec.size();i++){
        for(int j=0;j<vec[i].size();j++){
            cout<<vec[i][j]<<" ";
        }
        cout<<endl;

    }
 
    // Define 10x20 with all zeros
    vector<vector<int>> vec1(10,vector<int>(20,0));

    // Define 2d vector
    vector<int> vec2[4];







    return 0;
}