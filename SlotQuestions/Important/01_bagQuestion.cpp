#include<bits/stdc++.h>
using namespace std;
int main() {
    long long int x,y;
    cin >> x >> y;
    long long int sum = x + y,val = 1;
    while((val * (val + 1)) / 2 < sum) {
        val++;
    }
    if((val * (val + 1)) / 2 != sum) {
        cout << -1 << endl;
    }
    else {
        set<int> s,s1;
        int res = val;
        if(x >= y) {
            while(x > 0) {
                if(x - res >= 0) {
                    s.insert(res);
                    x -= res;
                    res--;
                }
                else {
                    s1.insert(res);
                    res--;
                }
            }
        }
        else {
            while(y > 0) {
                if(y - res >= 0) {
                    s1.insert(res);
                    y -= res;
                    res--;
                }
                else {
                    s.insert(res);
                    res--;
                }
            }
        }
        cout << s.size() << endl;
    }
}