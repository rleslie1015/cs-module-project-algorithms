import time

# Dynamic Programming
#   2 approaches 

#       Top Down --> Memoization 

def calc_time():
    print(f'\nResult calculated in {time.time()- start:5f}')

def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n-2)


start = time.time()
print(fib(30))
calc_time()

def memo_fib(n, memo):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return n
    
    memo[n] = memo_fib(n - 1, memo) + memo_fib(n-2, memo)
    return memo[n]

start = time.time()
print(memo_fib(309, {}))

calc_time()