memoF: list[int] = [0,1,1] + [0]*9
def fibonacci (num: int, memo: list[int]) -> int:
    if num <= 2: return memo[1]
    elif memo[num] != 0: 
        return memo[num]
    fib_n: int = fibonacci(num-2, memo) + fibonacci(num-1, memo)
    memo.insert(num, fib_n)
    return fib_n
    
print(fibonacci (5,memoF))