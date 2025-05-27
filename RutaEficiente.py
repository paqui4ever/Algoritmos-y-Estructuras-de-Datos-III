def solve (capacidad: int, distaciaM: int, estaciones: list[int]):
    estaciones_visitadas: list[int] = [0] # Siempre cargo en la primera
    cantidad_estaciones: int = 1 # Siempre cargo en al menos una

    for i in range (len(estaciones)-1):
        if estaciones [i] < capacidad and estaciones[i+1] >= capacidad: # Si el km en el que estoy no me paso de capacidad pero el siguiente si, entonces cargo antes de quedarme sin
            cantidad_estaciones += 1
            estaciones_visitadas.append(estaciones[i])
            capacidad += estaciones[i] # Ya pase la capacidad, sumo el km actual en que cargue asi tengo un nuevo "techo" de capacidad

    return estaciones_visitadas, cantidad_estaciones


print(solve(10, 20, [0, 4, 7, 9, 14, 17, 20]))