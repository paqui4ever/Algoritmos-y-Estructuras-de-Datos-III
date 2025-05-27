def solve (lista: list[int], target_length: int) -> list[int]:
    max_lista: list[int] = []
    ordenada = sorted(lista, reverse=True)
    res: int = 0
    for numero in ordenada:
        if len(max_lista) < target_length:
            res += numero
            max_lista.append(numero)

    return res, max_lista

print(solve([3, 1, 4, 1, 5, 9], 3))
