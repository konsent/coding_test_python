import sys

N = int(sys.stdin.readline())
count = 1
for i in range(N):
    print("*" * (count + i))