#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> memo;

int knapsack_topdown(vector<int>& w, vector<int>& v,
                                        int i, int W) {
    if (i == 0 || W == 0) return 0;
    if (memo[i][W] != -1) return memo[i][W];
    int res = knapsack_topdown(w, v, i - 1, W); // no tomar
    if (w[i - 1] <= W) { // tomar
        res = max(res, knapsack_topdown(w, v, i - 1, 
                                 W - w[i - 1]) + v[i - 1]); 
    }
    return memo[i][W] = res;
}

int main() {
	vector<int> w = {1, 2, 3, 4, 5};
	vector<int> v = {10, 15, 40, 50, 60};
	int W = 8;

	memo.assign(w.size() + 1, vector<int>(W + 1, -1));

	cout << knapsack_topdown(w, v, w.size(), W) << endl;
}

