import sys

N = int(sys.stdin.readline())
listA = []
for i in range(N):
    listA.append(int(sys.stdin.readline()))


for i in range(len(listA)):
    for j in range(len(listA)):
        if listA[i] < listA[j]:
            listA[i], listA[j] = listA[j], listA[i]

for n in listA:
    print(n)