import math
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

# Is Prime
def is_prime(n):
    return (prime(n,int(math.sqrt(n))))

def prime(n,count):
    if count == 0 or n == 1:
        return False
    if count == 1:
        return True
    if n % count == 0:
        return False
    return prime(n,count-1)

i = 8
print('fib(',i,') =',fib(i))
print('factorial(',i,') =',factorial(i))
i = 53
print('is_prime(',i,') =',is_prime(i))
