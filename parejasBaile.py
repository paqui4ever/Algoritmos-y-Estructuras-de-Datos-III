def solve (conjunto1: list[int], conjunto2: list[int]) -> int:
    ordenado1: list[int] = sorted(conjunto1)
    ordenado2: list[int] = sorted(conjunto2)
    parejas: list[int] = []
    res: int = 0
    for persona1, persona2 in zip(ordenado1, ordenado2):
        if abs(persona1 - persona2) <= 1:
            #conjunto2.remove(persona2)
            #conjunto1.remove(persona1)
            parejas.append((persona1, persona2))
            res += 1
    return res, parejas

print(solve([1,2,4,6], [1,5,5,7,9]))
print(solve([1,1,1,1,1], [1,2,3]))