import sys

N = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))

sortedA = sorted(set(listA)) # 리스트 값을 집합으로 중복을 없애고 정렬한다
result = {sortedA[i]:i for i in range(len(sortedA))} # .index는 O(N)이므로 시간초과가 뜨니까
# Dict로 키-밸류 쌍을 만들어서 주어진 값:주어진 값을 중복 없이 정렬했을 때의 인덱스' 로 저장한 뒤 거기서 참조한다
for i in listA:
    print(result[i], end=" ")