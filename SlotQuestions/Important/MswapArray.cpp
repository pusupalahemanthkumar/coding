#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int nSk(int n, int k){
    if (n < 2)
        return 1;
    if (k > n-2)
        return 0;
    vector<int> numbers;
    numbers.reserve(n - 2);
    for (int i = 0; i < n - 2; ++i){
        numbers.push_back(i + 2);
    }
    std::vector<bool> v(numbers.size());
    std::fill(v.end() - k, v.end(), true);
    int ret = 0;
    do {
        int tmpnum = 1;
        for (int j = 0; j < numbers.size(); ++j) {
            if (v[j])
            {
                tmpnum *= numbers[j];
            }
        }
        ret += tmpnum;
    } while (std::next_permutation(v.begin(), v.end()));
    return ret;
}
int main(){
    int n, d;
    cin >> n;
    cin >> d;
    int sum = 0;
    for (int k = 0; k < d; ++k){
        sum += nSk(n, k);
    }
    //sum *= 2;
    cout<< sum;
}
