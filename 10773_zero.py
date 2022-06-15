import sys
listA = []
K = int(sys.stdin.readline())

for i in range(K):
    a = int(sys.stdin.readline())
    if a == 0:
        listA.pop()
    else:
        listA.append(a)

result = 0
for i in listA:
    result += i

print(result)
