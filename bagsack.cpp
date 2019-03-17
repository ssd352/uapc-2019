#include <iostream>
#include <vector>

using namespace std;

int main(){
    long long n, W;
    cin >> n >> W;
    vector <long long> wi(n), vi(n);
    vector <vector <long long> > max_val(n + 1, vector<long long>(W + 1, 0));
    // long long max_val[100000001][21];
    for (int cnt = 0; cnt < n; cnt++){
        cin >> wi[cnt] >> vi[cnt];
    }
    for (long long current_weight = 1; current_weight <= W; current_weight++){
        long long max_ = 0;
        for (long long cnt = 0; cnt < n; cnt++){
            if (wi[cnt] > current_weight) continue;
            max_ = max_val[cnt][current_weight];
            if (max_ < max_val[cnt][current_weight - wi[cnt]] + vi[cnt]){
                max_ = max_val[cnt][current_weight - wi[cnt]] + vi[cnt];
            }
            max_val[cnt + 1][current_weight] = max_;

        }
    // max_val[current_weight] = max_;
    // cout << max_ << " ";
    }
    cout << max_val[n][W] << endl;
    return 0;
}