#include <iostream>
#include <vector>

using namespace std;
vector<vector<int>> memo;

int binomial_topdown(int n, int k) {
    if (k == 0 || k == n) return 1; // Caso base
    if (memo[n][k] != -1) return memo[n][k];
    return memo[n][k] = binomial_topdown(n - 1, k - 1) 
                        + binomial_topdown(n - 1, k);
}
int main() {
    int n = 10, k = 2;
    memo.assign(n + 1, vector<int>(k + 1, -1));
    cout << "C(" << n << ", " << k << ") = " 
    << binomial_topdown(n, k) << endl;
}


