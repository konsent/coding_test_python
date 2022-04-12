import sys

x_cord = []
y_cord = []

for _ in range(3):
    x, y = map(int,sys.stdin.readline().split())
    x_cord.append(x)
    y_cord.append(y)

for i in range(3):
    if x_cord.count(x_cord[i]) == 1:
        x = x_cord[i]
    if y_cord.count(y_cord[i]) == 1:
        y = y_cord[i]

print(x, y)