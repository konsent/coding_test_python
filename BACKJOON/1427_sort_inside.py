import sys

N = int(sys.stdin.readline())

listA = []

for i in str(N):
    listA.append(int(i))

listA.sort(reverse=True)

for i in listA:
    print(i, end="")

