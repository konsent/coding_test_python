import sys

X = int(sys.stdin.readline().rstrip())

total = 0

if len(str(X)) <= 2:
    total = X
elif len(str(X)) <= 4:
    total = 99
    count = 100
    while count <= X:
        gap = int(str(count)[1]) - int(str(count)[0])
        if int(str(count)[1]) + gap == int(str(count)[2]):
            total += 1
        count += 1

print(total)




