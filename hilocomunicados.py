numero_combinatorio_memo: list[list[int]] = []
def numero_combinatorio (n: int, k: int, memo: list[list[int]]) -> int:
    if k == 0 or k == n: return 1
    if n < k or k < 0: return 0
    elif memo[n][k] != -1: return memo[n][k]
    return numero_combinatorio(n - 1, k - 1, memo) + numero_combinatorio(n - 1, k, memo)


def calcular_probabilidad () -> int:
    res: int = 0
    string1: str = input()
    string2: str = input()

    total_enviado: int = 0

    for char in string1:
        if char == "+": total_enviado += 1
        elif char == "-": total_enviado -= 1
    
    total_recibido: int = 0
    inciertos: int = 0

    for char in string2:
        if char == "+": total_recibido += 1
        elif char == "-": total_recibido -= 1
        elif char == "?": inciertos += 1

    total_posibilidades = 2 ** (inciertos)

    faltan: int = total_enviado - total_recibido

    a_acomodar: int = (faltan + inciertos) // 2
    numero_combinatorio_memo = [[-1 for _ in range (a_acomodar+1)] for _ in range (inciertos+1)] # Inicializo mi lista con -1's para poder identificar los valores NO guardados
    res = numero_combinatorio (inciertos, a_acomodar, numero_combinatorio_memo) / total_posibilidades
    if a_acomodar < 0 or a_acomodar > inciertos: res = float(0) # Como mucho a_acomodar puede ser igual a inciertos, porque sino ya no tengo espacios disponibles para llegar al numero deseado
    print (res)

calcular_probabilidad()