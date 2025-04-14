def min_ignore (a: int, b: int) -> int:
    if a == None: return b
    elif b == None: return a 
    else: min(a,b) 

memo = {}

def coin_change (target: int, monedas: list[int], memo) -> int:
    if target == 0: res += 1
    res = 0
    for moneda in monedas:
        target_parcial = target - moneda
        if target_parcial < 0: continue
        if (moneda, target) not in memo: 
            memo[(moneda,target)] = target_parcial

        else: min_ignore(res, coin_change(memo[(moneda,target)], monedas) + 1)
            
        #else: min_ignore(res, coin_change(target_parcial, monedas) + 1)
    return res
        
print(coin_change(9, [1,4,5], {}))