import sys

T = int(sys.stdin.readline())

for i in range(T):
    R, S = sys.stdin.readline().split()
    for i in str(S):
        print(i * int(R), end="")
    print()

