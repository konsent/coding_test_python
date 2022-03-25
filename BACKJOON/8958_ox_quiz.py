import sys

N = int(sys.stdin.readline())

for _ in range(N):
    case = list(sys.stdin.readline())
    total = 0
    sum_modifier = 1
    for i in case:
        if i == 'O':
            total += sum_modifier
            sum_modifier += 1
        else:
            sum_modifier = 1
    print(total)