memo = {}
def potenciaLog(a: int, b: int) -> int:
    # Casos base
    if b == 0: return 1
    if b == 1: return a

    if (a, b) in memo:
        return memo[(a,b)]
        
    medioB = b // 2
    memo[(a, medioB)] = potenciaLog(a, medioB)
    if b % 3 == 0: return memo[(a, medioB)] * memo[(a, medioB)] * a  # Si es potencia impar la divido como una par por una potencia a la 1
    else: return memo[(a, medioB)] * memo[(a, medioB)] # Sino la divido en 2, pues es par
    return res


print(potenciaLog(2, 4))
print(potenciaLog(5, 3))