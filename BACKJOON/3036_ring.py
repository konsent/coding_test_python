import sys
import math

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(listA)):
    print("%d/%d" % (listA[0] // math.gcd(listA[0],listA[i]), listA[i] // math.gcd(listA[0],listA[i]) ))
