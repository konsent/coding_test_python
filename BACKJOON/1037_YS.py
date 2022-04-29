import sys

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))

print(max(listA)*min(listA))