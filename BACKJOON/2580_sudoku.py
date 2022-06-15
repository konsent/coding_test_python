import sys

array = []
for i in range(9):
    a = list(map(int,sys.stdin.readline().split()))
    array.append(a)


def horizon():
    for i in array:
        if i.count(0) == 1:
            for j in range(1, 10):
                if j not in a:
                    i[i.index(0)] = j


def vertical():
    for i in range(9):
        a = []
        for j in range(9):
            a.append(array[i][j])
            if a.count(0) == 1:
                for k in range(1,10):
                    if k not in a:
                        array[i][a.index(0)] = k

horizon()
vertical()
horizon()
vertical()

for i in range(9):
    for j in array[i]:
        print(j, end=" ")
    print("")


