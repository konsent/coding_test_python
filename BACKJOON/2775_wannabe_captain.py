import sys, math

T = int(sys.stdin.readline())

def sum2(floor, line):
    count = 0
    if floor == 1:
        return (line * (line + 1)) / 2
    for i in range(1, line+1):
        count += sum2(floor - 1, i)
    return count

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(int(sum2(k, n)))
