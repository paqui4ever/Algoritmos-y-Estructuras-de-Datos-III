from functools import lru_cache

def max_cajas_apilables(pesos, soportes):
    N = len(pesos)

    @lru_cache(maxsize=None)
    def dp(i, capacidad):
        if i == N:
            return 0

        # Opción 1: no uso la caja i
        mejor = dp(i + 1, capacidad)

        # Opción 2: uso la caja i (si no excede la capacidad)
        if pesos[i] <= capacidad:
            nueva_cap = min(capacidad - pesos[i], soportes[i])
            mejor = max(mejor, 1 + dp(i + 1, nueva_cap))

        return mejor

    # Capacidad inicial infinita (no hay caja debajo)
    return dp(0, float('inf'))

#print(max_cajas_apilables([19,7,5,6,1],[15,13,7,8,2]))

a = [1,2,3,4,5,6]

for v,w in a:
    print(v,w)
