def solve (monedas: list[int], target:int) -> list[int]:
    monedas_menor_a_mayor = filter(lambda x: False if x > target else True, reversed(sorted(monedas)))
    cantidad_de_monedas: int = 0
    res: list[int] = []
    if target == 0: return res
    for moneda in monedas_menor_a_mayor:
        while moneda <= target: # Clave para seguir usando monedas para llegar hasta target exactamente!
            target -= moneda
            res.append(moneda)
            cantidad_de_monedas += 1
    return res


print(solve([1,5,10,15,20], 13))

