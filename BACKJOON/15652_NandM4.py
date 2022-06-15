import sys

n, m = map(int, sys.stdin.readline().split())

s = []


def dfs():
    if len(s) > 1:
        if s[len(s)-1] < s[len(s)-2]:
            return
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()
