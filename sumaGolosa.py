import heapq

def solve (lista: list[int]) -> int:
    heapq.heapify(lista) # Paso a un min heap la lista
    total: int = 0

    while len(lista) > 1:
        # Saco los dos mas chicos
        x = heapq.heappop(lista)
        y = heapq.heappop(lista)
        costo = x + y 
        total += costo
        heapq.heappush(lista, costo) # Pongo en el heap la suma, asi despues saco eso y queda como acumulador para sumarselo al siguiente
    return total


print(solve([4, 3, 2, 6]))