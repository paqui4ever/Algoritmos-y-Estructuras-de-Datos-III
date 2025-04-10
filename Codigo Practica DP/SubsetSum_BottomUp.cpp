#include <iostream>
#include <vector>
using namespace std;

bool subset_sum(const vector<int>& S, int T) {
    int n = S.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(T + 1, false));
    dp[0][0] = true; // caso base
    for (int i = 1; i <= n; ++i) {
        for (int t = 0; t <= T; ++t) {
            dp[i][t] = dp[i-1][t]; // no tomar
            if (t >= S[i-1])        // tomar
                dp[i][t] = dp[i][t] || dp[i-1][t - S[i-1]]; 
        }
    }
    return dp[n][T];
}

int main() {
    vector<int> S = {3, 34, 4, 12, 5, 2};
    int T = 9;

    cout << (subset_sum(S, T) ? "Si" : "No")
         << " hay subconjunto con suma " << T << endl;
}
