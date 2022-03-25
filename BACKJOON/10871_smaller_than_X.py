import sys

n, x = map(int, sys.stdin.readline().split())
listA = list(map(int, sys.stdin.readline().split()))


for i in listA:
    if i < x:
        print(i, end=" ")
