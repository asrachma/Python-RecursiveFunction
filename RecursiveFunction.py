# Fibonacci number
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

# Factorial
def factorial(n):
    if n<= 1:
        return 1
    return factorial(n-1) * n



i = 8
print('fib(',i,') =',fib(i))
print('factorial(',i,') =',factorial(i))
