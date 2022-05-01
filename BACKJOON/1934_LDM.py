import sys

def lcm(a, b):
    listA = [a, b]
    listA.sort(reverse=True)
    while listA[1] != 0:
        listA[0], listA[1] = listA[1], listA[0] % listA[1]
    return a*b/listA[0]

T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(int(lcm(a, b)))
