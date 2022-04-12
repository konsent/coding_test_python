import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

n = int((V - A) / (A - B))

if (((n + 1) * A) - (n * B)) >= V:
    print(int(n+1))
else:
    print(int(n+2))