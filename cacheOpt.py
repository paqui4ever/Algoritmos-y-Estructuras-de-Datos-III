import heapq 
from collections import deque 

def solve (k: int, R: list[int]):
    siguientes_usos: list[int] = [float("inf")] * len(R)
    futuros_usos: dict[deque] = {}
    misses: int = 0

    for index, request in enumerate(R):
        if request not in futuros_usos:
            futuros_usos[request] = deque()
            futuros_usos[request].append(index)
        else: futuros_usos[request].append(index) # Agrego los indices en los que aparece cada request

    for i in range(len(R)):
        futuros_usos[R[i]].popleft() # Saco los indices en los que aparece por primera vez
        if futuros_usos[R[i]]: siguientes_usos[i] = futuros_usos[R[i]][0] # Si no esta vacia la queue, entonces le asigno
                                                                          # la posicion de la proxima vez que se usa (por eso [0]) 
    
    cache = set()
    heap = [] # Es min-heap asi que voy a tener que usar -siguientes_usos[i]
              # El valor mas grande, o sea el de mayor prioridad a sacar, tendrá el valor negativo más grande, por tanto más minimo y de mayor prioridad en el min-heap
              # Toma tuplas, y ordena por primer elemento, por tanto -siguientes_usos[i] será el primer elemento de las mismas
    for i in range(len(R)):
        request: int = R[i]
        next_element: float = siguientes_usos[i]

        if request not in cache:
            misses += 1
            if len(cache) < k:
                heapq.heappush(heap, (-next_element, request))
            else:
                while heap: 
                    _, old = heapq.heappop(heap) # Saco el de mayor prioridad, el que se usa mas tarde de todos
                    if old in cache: 
                        print("Saco {0}".format(old))
                        cache.remove(old)
                        break # IMPORTANTE: Sino seguiría sacando elementos del heap. Pongo el while para seguir sacar elementos que SI estan en la cache
                              # No necesariamente estan actualizados los valores del heap, puede haber entradas duplicadas (no estoy muy seguro de esto)
            print("Agrego {0}".format(request))
            cache.add(request)
            heapq.heappush(heap, (-next_element, request))  

    return misses

print(solve(2, [1,2,3,1]))
    

"""
from collections import deque
from ordered_set import OrderedSet

def solve (k: int, R: list[int]):
    r_orderedSet = OrderedSet()
    capacidad: int = 0
    cantidad_apariciones = []
    no_repetidos: list[int] = []
    repetidos: list[int] = []
    misses: int = 0

    for request in R: 
        if request not in no_repetidos: no_repetidos.append(request)
        else: 
            no_repetidos.remove(request)
            repetidos.append(request)

    for request in R:
        #print(request)
        #print(r_orderedSet, misses)
        if request not in r_orderedSet: misses += 1
        if capacidad < k:
            r_orderedSet.add(request)
            capacidad += 1
        else: 
            if r_orderedSet[-1] in no_repetidos:
                print(r_orderedSet) 
                r_orderedSet.pop()
                print(r_orderedSet)
                r_orderedSet.add(request)
            capacidad -= 1


    print(misses, r_orderedSet)

def numero_de_apariciones (elem: int, lista: list[int]):
    res: int = 0
    for elemento in lista:
        if elem == elemento: res += 1
    return res

solve(2, [1,2,3,2,3,3,1])
"""
