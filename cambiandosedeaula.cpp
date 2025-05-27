#include <iostream>
#include <vector>
#include <unordered_map>
#include <tuple>
#include <string>
#include <cstdlib>

using namespace std;

struct Key {
    int i, j, suma;

    bool operator==(const Key &other) const {
        return i == other.i && j == other.j && suma == other.suma;
    }
};

struct KeyHash {
    size_t operator()(const Key &k) const {
        return hash<int>()(k.i) ^ hash<int>()(k.j << 1) ^ hash<int>()(k.suma << 2);
    }
};

bool caminoMinimo(int i, int j, int suma,
                  const vector<vector<int>> &matriz,
                  int filas, int cols,
                  unordered_map<Key, bool, KeyHash> &memo) {
    if (i >= filas || j >= cols)
        return false;

    suma += matriz[i][j];

    if (abs(suma) > filas + cols)
        return false;

    if (i == filas - 1 && j == cols - 1)
        return suma == 0;

    Key k{i, j, suma};
    if (memo.find(k) != memo.end())
        return memo[k];

    bool res = caminoMinimo(i + 1, j, suma, matriz, filas, cols, memo) ||
               caminoMinimo(i, j + 1, suma, matriz, filas, cols, memo);

    memo[k] = res;
    return res;
}

int main() {
    int cantidadDeCasos;
    cin >> cantidadDeCasos;

    while (cantidadDeCasos--) {
        int filas, cols;
        cin >> filas >> cols;

        vector<vector<int>> matriz(filas, vector<int>(cols));
        for (int i = 0; i < filas; ++i) {
            for (int j = 0; j < cols; ++j) {
                cin >> matriz[i][j];
            }
        }

        if ((filas % 2 == 0 && cols % 2 == 0) || (filas % 2 != 0 && cols % 2 != 0)) {
            cout << "NO" << endl;
            continue;
        }

        unordered_map<Key, bool, KeyHash> memo;
        if (caminoMinimo(0, 0, 0, matriz, filas, cols, memo)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
