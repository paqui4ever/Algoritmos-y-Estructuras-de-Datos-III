#include <iostream>
#include <vector>
using namespace std;

long long factorial(int n, vector<long long>& memo) {
    if (memo.size() <= n) { memo.resize(n + 1, -1); }

    if (memo[n] != -1) { return memo[n]; }

    if (n <= 1) { return 1; }

    memo[n] = n * factorial(n - 1, memo);
    return memo[n];
}


int main() {
    int n = 10;
    vector<long long> memo(n + 1, -1);

    cout << n << "! es: " << factorial(n, memo) << endl;

    cout << "Valores memorizados en el vector:" << endl;
    for (int i = 0; i <= n; i++) {
        if (memo[i] != -1) {
            cout << i << "! = " << memo[i] << endl;
        }
    }
    return 0;
}


