# 재귀 함수
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print('fib 10', fib(10))

def countdown(n):
    if n <= 0:
        print('끝')
        return
    print(n)
    countdown(n - 1)

if __name__ == '__main__':
    print('fact', factorial(6))
