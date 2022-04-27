import sys

N =int(sys.stdin.readline())
listA = []

for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    listA.append([int(age),i,name])

listA.sort()

for i in listA:
    print(i[0], i[2])

