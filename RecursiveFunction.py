# Fibonacci number
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

i = 8
print('fib(',i,') =',fib(i))
i = 10
print('fib(',i,') =',fib(i))
i = 0
print('fib(',i,') =',fib(i))
