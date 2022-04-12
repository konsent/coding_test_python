import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

prime_num = []

for i in range(M, N + 1):
    err = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                err += 1
        if err == 0:
            prime_num.append(i)

if len(prime_num) == 0:
    print(-1)
else:
    sum = 0
    for i in prime_num:
        sum += i
    print(sum)
    print(min(prime_num))
