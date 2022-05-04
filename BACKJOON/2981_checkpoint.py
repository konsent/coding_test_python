import sys

N = int(sys.stdin.readline())
listA = []
for i in range(N):
    listA.append(int(sys.stdin.readline()))

def sosu(n):
    for i in range(n,0,-1):
        for dividend in range(2,int(i**0.5) + 1):
            if i % dividend == 0:
                break
        return i

result = []
for j in range(2, sosu(min(listA))+1):
    listB = set()
    for i in listA:
        listB.add(i % j)
    if len(listB) == 1:
        print(j, end=" ")

