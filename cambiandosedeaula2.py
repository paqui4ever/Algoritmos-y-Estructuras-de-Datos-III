def cambiandoseDeAula():
    cantidad_de_casos = int(input())
    resultados = [] 

    for _ in range(cantidad_de_casos):
        filas, cols = map(int, input().split())

        matriz = []
        for _ in range(filas):
            fila = list(map(int, input().split()))
            matriz.append(fila)

        if filas % 2 == 0 and cols % 2 == 0: 
            print("NO")
            continue
        elif filas % 2 != 0 and cols % 2 != 0: 
            print("NO")
            continue

        minimo = [[float('inf')] * cols for _ in range(filas)]
        maximo = [[-float('inf')] * cols for _ in range(filas)]
        minimo[0][0] = maximo[0][0] = matriz[0][0]

        for i in range(filas):
            for j in range(cols):
                if i > 0:
                    minimo[i][j] = min(minimo[i][j], minimo[i - 1][j] + matriz[i][j])
                    maximo[i][j] = max(maximo[i][j], maximo[i - 1][j] + matriz[i][j])
                if j > 0:
                    minimo[i][j] = min(minimo[i][j], minimo[i][j - 1] + matriz[i][j])
                    maximo[i][j] = max(maximo[i][j], maximo[i][j - 1] + matriz[i][j])

        if minimo[filas - 1][cols - 1] <= 0 <= maximo[filas - 1][cols - 1]: print("YES")
        else: print("NO")

cambiandoseDeAula()