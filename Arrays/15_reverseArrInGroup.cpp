#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,k;
    cin>>n>>k;
    vector<int> a;
    for(int i=0;i<n;i++){
        int t;
        cin>>t;
        a.push_back(t);
    }
    // Main Logic
    for(int i=0;i<n;i+k){
        int start=i;
        int end=min(i+k-1,n-1);
        while(start<=end){
            int t=a[start];
            a[start]=a[end];
            a[end]=t;
            start++;
            end--;
        }
    }
    for(auto i:a){
        cout<<i<<" ";
    }
    return 0;
}