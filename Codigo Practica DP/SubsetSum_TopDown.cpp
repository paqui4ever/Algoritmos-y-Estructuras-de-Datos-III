#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>> memo; // -1: no calculado, 0: false, 1: true

bool subset_sum_topdown(const vector<int>& S, int i, int t) {
    if (t == 0) return true;
    if (i == 0) return false;
    if (memo[i][t] != -1) return memo[i][t];

    bool res = subset_sum_topdown(S, i - 1, t);
    if (t >= S[i - 1])
        res = res || subset_sum_topdown(S, i - 1, t - S[i - 1]);
    return memo[i][t] = res;
}

int main() {
    vector<int> S = {3, 34, 4, 12, 5, 2};
    int T = 9;
    memo.assign(S.size() + 1, vector<int>(T + 1, -1));

    cout << (subset_sum_topdown(S, S.size(), T) ? "Si" : "No")
         << " hay subconjunto con suma " << T << endl;
}