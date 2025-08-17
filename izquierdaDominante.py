def izquierdaDominante (lista: list[int]) -> bool:
    size = len(lista)

    lista1, lista2 = subArray(lista, 2)

    if len(lista) == 2: 
        if lista1[0] <= lista2[0]: 
            return False
        else: return True

    #sumaVale: bool = sum(lista1) > sum(lista2) 
    while sum(lista1) > sum(lista2):
        return izquierdaDominante(lista1) and izquierdaDominante(lista2)
    else: return False
    

def subArray (lista: list[int], dividoEn: int) -> list[int]:
    res1 = []
    res2 = []
    indiceParaPartir = len(lista) / dividoEn
    for i in range (len(lista)):  
        if i <= indiceParaPartir - 1:
            res1.append(lista[i])
        else: res2.append(lista[i])
    return res1, res2 

print(izquierdaDominante([8,4,7,6,5,1,3,2]))
print(izquierdaDominante([10, 5, 2, 1, 3, 2, 1, 0]))
print(izquierdaDominante([6, 4, 5, 3, 2, 2, 1, 1]))
