def rutaMinima (D: list[list[int]]):
    res = []
    dictPermutacionesValores = {}
    permutacionesHechas = set()
    elementosVistos = []
    permutacionActual = []


    def backtrack (rutaActual: list[int], siguiente: int):

        if len(rutaActual) == len(D): 
            #rutaActual.append(rutaActual[0])
            permutacionesHechas.add(tuple(permutacionActual))
            return
        
        for i in range (len(D)): # O (|D|) = O (n)
            if i not in elementosVistos:
                elementosVistos.append(i) 
                permutacionActual.append(i)

                backtrack(permutacionActual, i+1) # Lo tomo como una llamada O(1) porque devuelve un valor (no estoy muy seguro de esto)

                elementosVistos.pop()
                if len(permutacionActual) != 0:
                    permutacionActual.pop()
                    #permutacionActual.pop() # Porque hay que sacar también al ultimo elemento que es igual al primero
                
                #backtrack(permutacionActual, i+1)

    backtrack([], 0)

    for permutacion in permutacionesHechas: # O (numero de permutaciones) = O(n!)
        suma_weights = 0
        for i in range(len(permutacion)-1):
            suma_weights += D[permutacion[i]][permutacion[i+1]]
        dictPermutacionesValores[permutacion] = suma_weights

    min = 1000

    for permutacion in dictPermutacionesValores: # O (numero de permutaciones) = O(n!)
        if dictPermutacionesValores[permutacion] <= min:
            min = dictPermutacionesValores[permutacion]
            res = list(permutacion)
    
    return res

# Total = O (n!)
            
print(rutaMinima([[0,1,10,10],[10,0,3,15],[21,17,0,2],[3,22,30,0]]))