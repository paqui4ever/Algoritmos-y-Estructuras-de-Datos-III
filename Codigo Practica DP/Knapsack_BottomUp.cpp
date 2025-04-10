#include <iostream>
#include <vector>
using namespace std;

int knapsack(const vector<int>& weights, const vector<int>& values, int W) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int w = 0; w <= W; ++w) {
            dp[i][w] = dp[i-1][w]; // no tomar
            if (w >= weights[i - 1]) {
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i - 1]] + values[i - 1]); // tomar
            }
        }
    }
    return dp[n][W];
}


int main() {
	vector<int> weights = {1, 2, 3, 4, 5};
	vector<int> values = {10, 15, 40, 50, 60};
	int W = 8;
	cout << knapsack(weights, values, W) << endl; // Output: 55
	return 0;
}

