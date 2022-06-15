import sys

N,W,H = map(int,sys.stdin.readline().split())
for i in range(N):
    a = int(sys.stdin.readline())
    c = (W**2 + H**2)**0.5
    if a <= W or a <= H or a <= c:
        print("DA")
    else:
        print("NE")