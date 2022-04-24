import sys

N, M = map(int,sys.stdin.readline().split())

def white(M):
    count = 0
    stringW = "W"
    while count < (M-1):
        if stringW[count] == "W":
            stringW += "B"
        else:
            stringW += "W"
        count += 1
    return stringW
def black(M):
    count = 0
    stringB = "B"
    while count < (M-1):
        if stringB[count] == "B":
            stringB += "W"
        else:
            stringB += "B"
        count += 1
    return stringB
def whiteandblack(N, M):
    listA = []
    for i in range(N):
        if i % 2 == 0:
            listA.append(white(M))
        else:
            listA.append(black(M))
    return listA
def blackandwhite(N, M):
    listA = []
    for i in range(N):
        if i % 2 == 0:
            listA.append(black(M))
        else:
            listA.append(white(M))
    return listA

listA = []
for i in range(N):
    line = sys.stdin.readline().rstrip()
    listA.append(line)

def finalcomparison(n,m):
    countW = 0
    countB = 0
    for i in range(n, n+8):
        for j in range(m, m+8):
            if listA[i][j] != whiteandblack(N, M)[i][j]:
                countW += 1
    for i in range(n,n+8):
        for j in range(m,m+8):
            if listA[i][j] != blackandwhite(N, M)[i][j]:
                countB += 1
    return min(countB,countW)

listB = []
for n in range(0,N - 7):
    for m in range(0, M - 7):
        listB.append(finalcomparison(n, m))

print(min(listB))


