import sys

N = int(sys.stdin.readline())
count = 1
for i in range(1, N+1):
    print(" " * (N - i) + "*" * i)
