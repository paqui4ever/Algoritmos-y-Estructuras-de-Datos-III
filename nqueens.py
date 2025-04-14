def nqueens (n: int) -> list[list[int]]:
    board: list[list[int]] = [[0 for _ in range (n)] for _ in range(n)] # Armo mi board con list comprehensions

    columns: set = set()
    positive_diagonal: set = set() # row + col
    negative_diagonal: set = set() # row - col

    res: list[list[int]] = []

    def backtrack (row: int) -> list[list[int]]:
        if row == n: # Caso base: ya no hay mas filas por ver
             res.append([row[:] for row in board]) # Tengo que hacer una copia de cada fila porque sino termino perdiendo las soluciones
             return

        for i in range (n): 
                if i in columns or (i + row) in positive_diagonal or (row - i) in negative_diagonal: # Me fijo si es valida la posicion
                    continue
                
                columns.add(i)
                positive_diagonal.add(i + row)
                negative_diagonal.add(row - i)
                board[row][i] = 1 # Actualizo mi board

                backtrack (row + 1) # Paso recursivo, con la siguiente fila

                # Vuelvo para atras así contemplo todas las posibles soluciones 
                columns.remove(i) 
                positive_diagonal.remove(i + row)
                negative_diagonal.remove(row - i)
                board[row][i] = 0
    
    backtrack(0)
    return res

print(nqueens(4))