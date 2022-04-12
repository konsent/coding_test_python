import sys, math

T = int(sys.stdin.readline())

for _ in range(T):
    h, w, n = map(int, sys.stdin.readline().split())
    room_num = math.ceil(n / h)
    floor_num = n % h if n % h != 0 else h
    print(int("{}{}".format(floor_num, "0{}".format(room_num) if room_num < 10 else "{}".format(room_num))))

