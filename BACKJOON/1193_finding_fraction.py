import sys

X = int(sys.stdin.readline())

n = 1
while X > (n * (n + 1))/2:
    n += 1

count_adj = X - (n * (n - 1))/2

if (n % 2) == 1:
    print("%d/%d" % ((n - (count_adj - 1)),count_adj))
else:
    print("%d/%d" % (count_adj, (n - (count_adj - 1))))
