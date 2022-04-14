import math
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    # 원의 방정식으로 두 원 사이의 거리를 구한다
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif (r1 + r2) == distance or abs(r1 - r2) == distance:
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)

