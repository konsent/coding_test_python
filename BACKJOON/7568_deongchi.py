import sys

N = int(sys.stdin.readline())
listA = []
for _ in range(N):
    listA.append(list(map(int, sys.stdin.readline().split())))

for set in listA:
    grade = 1
    for set2 in listA:
        if set[0] < set2[0] and set[1] < set2[1]:
            grade += 1
    print(grade, end=" ")

