import sys

N, M = map(int, sys.stdin.readline().split())
listA = list(map(int, sys.stdin.readline().split()))

target_list = [i for i in listA if i < M]
result = []

for i in target_list:
    for j in target_list:
        if j != i:
            for k in target_list:
                if k != i and k != j:
                    sum = i + j + k
                    if sum <= M:
                        result.append(sum)

result.sort()
print(result.pop())
