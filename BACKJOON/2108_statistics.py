import sys
from collections import Counter

N = int(sys.stdin.readline())
listA = []
for _ in range(N):
    listA.append(int(sys.stdin.readline()))

listA.sort()


print(int(round(sum(listA)/len(listA), 0)))

print(listA[len(listA)//2])

cnt = Counter(listA).most_common(2)
if len(listA) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(abs(max(listA) - min(listA)))