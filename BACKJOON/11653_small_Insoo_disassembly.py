import sys

N = int(sys.stdin.readline())

dividend = []
dividend_idx = 0

for i in range(2, N+1):
    if N % i == 0:
        dividend.append(i)

while dividend_idx < len(dividend):
    if N % dividend[dividend_idx] == 0:
        print(dividend[dividend_idx])
        N /= dividend[dividend_idx]
    else:
        dividend_idx += 1


