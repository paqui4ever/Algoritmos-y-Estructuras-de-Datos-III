def magicCube (dim: int, M: list[int] = []):
    valoresP = set(range(1, dim**2+1)) # Armo mi set de valores posibles desde 1 hasta dim^2 INCLUSIVE (por eso el +1)
    res = []
    if not validate (dim, M[:]): return [] # Para validar uso LA COPIA (shallow copy) de la matriz original
    elif len(M) == dim ** 2: return [M]
    for num in valoresP:
        if num not in M: res += magicCube (dim, M + [num])
    return res


def validate (dim: int, M: list[int]):
    for _ in range (dim**2 - len(M)): M.append(0) # Lleno de 0's los lugares no completados en mi solucion parcial
    magicNum = (dim**3 + dim) / 2

    for i in range (dim):
        fila = [M[dim*i + j] for j in range (dim)] # Armo mi fila con una list comprehension
        if 0 not in fila: # Lo hago en diagonales, filas y columnas: me fijo que si esta completa que la suma de los elementos sea igual a numero magico
            if sum(fila) != magicNum: return False
        elif sum(fila) > magicNum: return False

    for i in range (dim):
        row = [M[dim*j + i] for j in range (dim)] # Armo mi columna con una lista comprehension
        if 0 not in row:
            if sum(row) != magicNum: return False
        elif sum(row) > magicNum: return False

    diagonal1 = [M[dim*i + i] for i in range (dim)] # Armo mi primera diagonal de izquierda a derecha
    if 0 not in diagonal1:
        if sum(diagonal1) != magicNum: return False 
    elif sum(diagonal1) > magicNum: return False

    diagonal2 = [M[(dim - 1) * (i + 1)] for i in range (dim)] # Armo mi segunda diagonal, de derecha a izquierda
    if 0 not in diagonal2:
        if sum(diagonal2) != magicNum: return False
    elif sum(diagonal2) > magicNum: return False

    return True

print(magicCube(4))
    
        
            
