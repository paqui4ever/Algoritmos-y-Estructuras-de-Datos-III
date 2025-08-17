def indiceEspejo (lista: list[int], low: int, high: int) -> int:
    if low > high: return float("inf")
    mid = (high + low) // 2 # High y low son mis indices originales de comienzo y fin del subarray
    if lista[mid] == mid: return mid # Si se cumple la propiedad, ya está
    elif lista[mid] > mid: # Descarto la mitad derecha
        return indiceEspejo(lista, low, mid-1)
    else: # Descarto la mitad izquierda
        return indiceEspejo(lista, mid+1, high)

print(indiceEspejo([-4,1,3,4,7], 0, 5))