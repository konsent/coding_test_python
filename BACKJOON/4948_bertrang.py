import sys

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    result_count = 0

    for i in range(n+1, 2*n + 1):
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                break
        else:
            result_count += 1

    print(result_count)


