import sys

A, B, C = map(int, sys.stdin.readline().split())

n = 0

if C <= B:
    print(-1)
else:
    print((A // (C - B)) + 1)
