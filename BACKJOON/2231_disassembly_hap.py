import sys

N = int(sys.stdin.readline())

maxA = N - len(str(N)) * 1 if N - len(str(N)) * 1 < 0 else N
minA = N - len(str(N)) * 9 if N - len(str(N)) * 1 < 0 else 1


count = 0
for num in range(minA, maxA + 1):
    if num + sum(map(int, str(num))) == N:
        print(num)
        count += 1
        break

if count == 0:
    print(0)

