import sys

N = int(sys.stdin.readline())
listA = []
for _ in range(N):
    listA.append(sys.stdin.readline().rstrip())

temps = []
result = []

for i in range(1, 51):
    for j in listA:
        if len(j) == i and j not in temps:
            temps.append(j)
    temps.sort()
    while len(temps) != 0:
        result.append(temps.pop(0))

for i in result:
    print(i)

