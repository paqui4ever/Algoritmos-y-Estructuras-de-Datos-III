def maximaGananciaNeta (p: list[int]):
    def dp (c:int, j:int):
        if c < 0 or c > j: return float("-inf") # En j dias no puedo haber comprado mas de j asteroides
        if j < 0: 
            return 0 if c == 0 else float("-inf")
        
        opcion_compra = dp(c-1, j-1) - p[j]
        opcion_venta = dp(c+1,j-1) + p[j]
        opcion_nada = dp(c,j-1)

        return max(opcion_compra, opcion_venta, opcion_nada)

    return dp(0, len(p)-1)

print(maximaGananciaNeta([3,2,5,6]))