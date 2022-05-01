# import sys
#
# A, B = map(int, sys.stdin.readline().split())
# a, b = A, B
#
# while b != 0:
#     a, b = b, a % b
#
# print(a)
# print(int(A*B/a))

import sys

a, b = map(int, sys.stdin.readline().split())

gcm = 1
ldm = 1

def sosu(n):
    listA = []
    for i in range(2, n+1):
        notsosu = 0
        if n > 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    notsosu += 1
            if notsosu == 0:
                listA.append(i)
    return listA


while True:
    for i in sosu(10000):
        while a % i == 0 and b % i == 0:
            a /= i
            b /= i
            gcm *= i
    ldm = gcm * a * b
    break

print(int(gcm))
print(int(ldm))