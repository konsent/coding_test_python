import sys

x, y, w, h = map(int, sys.stdin.readline().split())

short_x = min(x, w - x)
short_y = min(y, h - y)
print(min(short_y,short_x))