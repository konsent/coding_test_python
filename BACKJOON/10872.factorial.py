import sys

N = int(sys.stdin.readline())


def facto(N):
    if N == 1:
        return 1
    if N == 0:
        return 1
    return N * facto(N - 1)


print(facto(N))
