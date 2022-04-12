import sys

N = int(sys.stdin.readline())

listA = []
for i in range((N // 5) + 1):
    for j in range((N // 3) + 1):
        if (5 * i) + (3 * j) == N:
            listA.append(i + j)

if len(listA) == 0:
    listA.append(-1)

print(min(listA))