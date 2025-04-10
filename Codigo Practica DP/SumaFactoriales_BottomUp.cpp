#include <iostream>
#include <vector>

using namespace std;

long long suma_de_factoriales(int n) {
    vector<long long> fact(n + 1, 1);
    vector<long long> sum(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        fact[i] = i * fact[i - 1];           // factorial
        sum[i] = sum[i - 1] + fact[i];       // suma acumulada
    }

    return sum[n];
}

int main() {
    int n = 10;
    cout << "Suma de factoriales hasta " << n << " es: "
         << suma_de_factoriales(n) << endl;
    return 0;
}
