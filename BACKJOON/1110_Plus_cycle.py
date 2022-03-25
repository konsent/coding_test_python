import sys

N = int(sys.stdin.readline().rstrip())
start_N = N
count = 0

while True:
    N = ((N // 10) + (N % 10)) % 10 + (N % 10) * 10
    count += 1
    if N == start_N:
        break


print(count)