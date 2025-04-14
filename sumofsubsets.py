def sumofsubsets (s: list[int], k: int):
    suma_actual: int = 0
    res: int = 0

    def backtrack(posicion: int):
        nonlocal suma_actual, res
                                                         
        if posicion == len(s): # Si ya recorrimos toda la lista y no llegamos a k, listo
            if suma_actual == k: # Se fija si es un resultado valido
                res += 1 
            return
        
        suma_actual += s[posicion] # Elijo incluir el elemento
 
        backtrack (posicion+1) # Hago backtracking sobre la rama de decision de incluirlo

        suma_actual -= s[posicion] # Elijo no incluirlo

        backtrack(posicion+1) # Hago backtracking sobre la rama de decision de no incluirlo

    backtrack(0)
    return res 

print(sumofsubsets([1,1,1,1],3))