import sys

N = int(sys.stdin.readline())

listA = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    listA.append((x, y))

listA.sort()
for i in listA:
    print(i[0],i[1])