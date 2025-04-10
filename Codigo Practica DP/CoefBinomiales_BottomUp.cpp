#include <iostream>
#include <vector>

using namespace std;

int binomial(int N, int K) {
    vector<vector<int>> dp(N + 1, vector<int>(K + 1, 0));
    for (int n = 0; n <= N; ++n) {
        for (int k = 0; k <= min(n, K); ++k) {
            if (k == 0 || k == n) // Caso base
                dp[n][k] = 1; 
            else  // Paso recursivo
                dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k]; 
        }
    }
    return dp[N][K];
}

int main() {
    int n = 10, k = 2;
    cout << "C(" << n << ", " << k << ") = " 
    << binomial(n, k) << endl;
}
