import sys


n = int(sys.stdin.readline())
memo = {
    0: 0,
    1: 1,
    2: 1
}


def fibo(n,memo):
    if n in memo:
        return memo[n]
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

print(fibo(n, memo))