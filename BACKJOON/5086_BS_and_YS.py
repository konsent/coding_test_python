import sys

while 1:
    a, b = map(int, sys.stdin.readline().split())
    if a > 0 and b > 0:
        if a % b == 0 and a > b:
            print('multiple')
        elif b % a == 0 and a < b:
            print('factor')
        else:
            print('neither')
    if a == 0 and b == 0:
        break

