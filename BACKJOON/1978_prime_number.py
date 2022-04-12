import sys

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))

count = 0

for given_num in listA:
    not_sosu = 0
    if given_num > 1:
        for dividend in range(2, given_num):
            if given_num % dividend == 0:
                not_sosu += 1
        if not_sosu == 0:
            count += 1

print(count)