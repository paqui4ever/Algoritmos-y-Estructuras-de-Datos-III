def cambiandoseDeAula ():
    cantidad_de_casos = int(input())
    resultados = []

    for _ in range(cantidad_de_casos):
        filas, cols = map(int, input().split())

        matriz = []
        for _ in range(filas):
            fila = list(map(int, input().split()))
            matriz.append(fila)

        if filas % 2 == 0 and cols % 2 == 0: 
            resultados.append("NO")
            continue
        elif filas % 2 != 0 and cols % 2 != 0: 
            resultados.append("NO")
            continue

        memo = {}
        def caminimoMinimo (i, j, suma):
            if i >= filas or i < 0 or j < 0 or j >= cols: # para que no se pasen los indices
                return False

            suma += matriz[i][j] # Voy sumando los weights

            if abs(suma) > filas + cols: return False 

            if i == filas - 1 and j == cols - 1: # Si llegamos al extremo inferior derecho me fijo si la suma acumulada da 0
                if suma == 0: return True
                else: return False

            clave_memo = (i, j, suma)
            if clave_memo in memo: return memo[clave_memo] # Si tengo la clave, devuelvo su valor guardado

            res = caminimoMinimo(i+1, j, suma) or caminimoMinimo(i, j+1, suma) # O voy a la derecha o a la izquierda

            memo[clave_memo] = res
            return res

        if caminimoMinimo(0,0,0): resultados.append("YES")
        else: resultados.append("NO")
        
    for resultado in resultados: 
        print(resultado)

cambiandoseDeAula()