import sys

listA = []

for i in range(9):
    a = int(sys.stdin.readline())
    listA.append(a)

print(max(listA))
print(listA.index(max(listA))+1)