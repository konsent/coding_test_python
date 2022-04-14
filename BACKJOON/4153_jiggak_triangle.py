import sys

while True:
    listA = list(map(int, sys.stdin.readline().split()))
    if listA == [0, 0, 0]:
        break
    else:
        listA.sort()
        max_length = listA.pop()
        if max_length**2 == listA[0]**2 + listA[1]**2:
            print("right")
        else:
            print("wrong")
