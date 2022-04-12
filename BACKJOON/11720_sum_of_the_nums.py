import sys

n = int(sys.stdin.readline().rstrip())
given_num = int(sys.stdin.readline())

total = 0
for i in str(given_num):
    total += int(i)

print(total)