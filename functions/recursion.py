# 재귀 함수
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
