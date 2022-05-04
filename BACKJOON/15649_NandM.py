# import sys
# from itertools import combinations, permutations
#
# N, M = map(int,sys.stdin.readline().split())
# listA = []
# for i in range(1,N+1):
#     listA.append(i)
#
# for i in permutations(listA,M):
#     for j in range(M):
#         print(i[j], end=" ")
#     print("")
#

# import sys
# N, M = map(int,sys.stdin.readline().split())
#
# s = []
#
# def f():
#     if len(s) == M:
#         print(' '.join(map(str,s)))
#         return
#
#     for i in range(1, N+1): # 1,2,3
#         if i in s:
#             continue
#         s.append(i)
#         f()
#         s.pop()
#
# f()

import sys
N, M = map(int,sys.stdin.readline().split())

s = []

def f():
    if len(s) == M:
        print(" ".join(map(str,s)))
        return
    for i in range(1, N+1):
        if i in s:
            continue
        s.append(i)
        f()
        s.pop()

f()