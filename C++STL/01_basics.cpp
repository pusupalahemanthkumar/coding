#include<bits/stdc++.h>
using namespace std;

namespace h{
    int val=50;
    // we can declare function even here
    int getVal(){
        return val*10;
    }
}

int main(){
    double val=10.0;

    cout<<val<<endl; // prints 10.0

    cout<<h::val<<endl; // prints 50

    cout<<h::getVal()<<endl; // prints 500

    return 0;
}