def maxisubconjunto (M: list[list[int]], k: int) -> list[int]:
    conjuntos_vistos = set()
    solucion_parcial: list[int] = []
    res: list[list[int]] = []

    # Parte en la que busco todas las soluciones validas

    def backtrack (cto: list[int], index: int):
        if len(cto) == k: # Caso base
            conjunto = frozenset(cto) # Hace que la lista sea una tupla dentro de un set
            if conjunto not in conjuntos_vistos: # Poda por optimalidad
                conjuntos_vistos.add(conjunto)
                res.append(list(conjunto))
                return
            
        for i in range (index, len(M)):
            if i not in cto:
                cto.append(i)
                backtrack (cto, i+1) # LLamada recursiva
                cto.pop() # Parte back del backtracking

    backtrack(solucion_parcial, 0)

    # Parte en la que busco la solucion optima

    sumas_tuplas: dict[tuple, int] = {}
    pares_vistos: dict[tuple, int] = {} # DP 

    for j in range(len(res)):
        suma = 0
        for i in range(len(res)):
            if (j,i) in pares_vistos.keys(): suma += pares_vistos[(j,i)] # Si ya tengo ese par, lo agarro del hashmap
            else: 
                pares_vistos[(j,i)] = M[j][i]
                suma += M[j][i] # Porque sé que es simetrica
    
        sumas_tuplas[tuple(res[j])] = suma

    max: int = 0
    sol_optima: list[int] = []

    for clave in sumas_tuplas:
        if sumas_tuplas[clave] >= max:
            max = sumas_tuplas[clave]
            sol_optima = list(clave)
    
    return sol_optima

A = [[0,10,10,1],[10,0,5,2],[10,5,0,1],[1,2,1,0]]
print(maxisubconjunto (A, 3))