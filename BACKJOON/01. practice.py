import sys

n = int(sys.stdin.readline())
total_sum = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

