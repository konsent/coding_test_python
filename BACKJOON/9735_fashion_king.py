import sys
from collections import defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    count = 1
    dictA = defaultdict(list)

    for _ in range(n):
        a = list(map(str,sys.stdin.readline().split()))
        dictA[a[1]].append(a[0])

    for i in dictA:
        count *= (len(dictA[i])+1)

    print(count-1)








