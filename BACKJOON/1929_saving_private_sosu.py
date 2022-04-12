import sys

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    not_sosu = 0
    if M > 1:
        for j in range(2, int(M**0.5)+1):
            if M % j == 0:
                not_sosu += 1
                break
        if not_sosu == 0:
            print(M)
    M += 1