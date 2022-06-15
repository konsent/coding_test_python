import sys

n, m = map(int, sys.stdin.readline().split())

s = []
ss = []
visited = [False]*(n+1)


def dfs():
    if len(s) == m:
        # a = list(map(str,s))
        # if set(a) in ss:
        #     return
        print(' '.join(map(str,s)))
        # ss.append(set(a))
        return

    for i in range(1,n+1):
        # if not visited[i]:
        #     visited[i] = True
            s.append(i)
            dfs()
            s.pop()
            # visited[i] = False

dfs()

