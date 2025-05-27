def calcular_probabilidad(): 
    res: int = 0
    string1: str = input()
    string2: str = input()

    total_enviado: int = 0
    total_recibido: int = 0
    cantidad_inciertos: int = 0

    for signo in string1:
        if signo == "+": total_enviado += 1
        else: total_enviado -= 1

    for signo in string2:
        if signo == "+": total_recibido += 1
        elif signo == "-": total_recibido -= 1
        else: cantidad_inciertos += 1

    diferencia_mensaje: int = abs(total_enviado - total_recibido)

    def backtrack (cant_signos_de_pregunta: int):
        if cant_signos_de_pregunta > diferencia_mensaje: return float(0)
        if 