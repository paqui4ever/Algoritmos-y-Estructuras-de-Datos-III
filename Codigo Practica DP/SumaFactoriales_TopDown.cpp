#include <iostream>
#include <vector>

using namespace std;

vector<long long> fact_memo;
vector<long long> sum_memo;

long long factorial(int n) {
    if (n == 0) return 1;
    if (fact_memo[n] != -1) return fact_memo[n];
    return fact_memo[n] = n * factorial(n - 1);
}

long long suma_factoriales(int n) {
    if (n == 0) return 0;
    if (sum_memo[n] != -1) return sum_memo[n];
    return sum_memo[n] = suma_factoriales(n - 1) + factorial(n);
}

int main() {
    int n = 10;
    fact_memo.assign(n + 1, -1);
    sum_memo.assign(n + 1, -1);

    cout << "Suma de factoriales hasta " << n << " es: "
         << suma_factoriales(n) << endl;

    return 0;
}
