def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# fibonacci(1)
# fibonacci(10)
#
# factorial(0)
# factorial(1)