import numpy as np

memoPotencia = {}
memoSuma = {}
def potenciaConMemo (A: list[list[int]], n: int) -> list[list[int]]:
    if n == 1: return A 
    if n in memoPotencia:
        return memoPotencia[n]
    mediaPotencia = np.linalg.matrix_power (A, n//2)
    memoPotencia[n//2] = mediaPotencia
    if n % 2 == 0:     
        return memoPotencia[n//2] @ memoPotencia[n//2] 
    else: return memoPotencia[n//2] @ memoPotencia[n//2] @ A 

def potenciaSuma (A: list[list[int]], n: int) -> list[list[int]]:
    if n == 1: return A 
    if n in memoSuma: return memoSuma[n]
    mitadN = n // 2
    I = np.identity(len(A), dtype = int)
    mediaPot = potenciaConMemo(A, mitadN)
    memoSuma[mitadN] = potenciaSuma (A, mitadN)
    return np.array(memoSuma[mitadN]) @ (I + np.array(mediaPot))

print(potenciaConMemo([[2,3],[3,2]], 2))
print(potenciaSuma([[2,3],[3,2]], 4))