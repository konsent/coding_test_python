import sys

T = int(sys.stdin.readline())


def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)


for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    a = 1
    for j in range(n):
        a *= (m - j)

    print(int(a/f(n)))
