def mex (lista: list[int]):
    not_in_lista: list[int] = []
    for i in range(len(lista)):
        if i not in lista: 
            not_in_lista.append(i)
    not_in_lista.append(lista[-1]+1) # Si no hay "gaps" agrego el que sigue al ultimo de la secuencia
    mex: int = min(not_in_lista) # Devuelvo siempre el min por def
    return mex

#print(mex([0,1,2]))

def solve (vector: list[int]):
    ordenado = sorted(vector) # De menor a mayor SIEMPRE obtengo el maximo resultado por mex
    lista_operaciones: list[int] = [] # Lista en la que voy poniendo de a uno los elementos para hacer los mex intermedios
    res: int = 0
    for numero in ordenado:
        lista_operaciones.append(numero)
        res += mex(lista_operaciones)
    return res

print(solve([3,0,1]))
print(solve([0, 1, 2, 5]))
print(solve([1,2,3,4]))
print(solve([5,5,5]))


