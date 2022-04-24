import sys

N = int(sys.stdin.readline())

print(2 ** N - 1)


def hanoi(n, start, temp, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, end, temp)
    print(start, end)
    hanoi(n - 1, temp, start, end)


hanoi(N, 1, 2, 3)
