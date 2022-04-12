import sys

# 테스트 케이스 개수
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    case = list(map(int, sys.stdin.readline().split()))
    total = 0
    avg = 0
    count = 0
    for i in case[1:]:
        total += i
    avg = total / case[0]

    for i in case[1:]:
        if i > avg:
            count += 1

    result = round((count / case[0] * 100),3)

    print("{:.3f}%".format(result))


