import sys

n, m = map(int,sys.stdin.readline().split())

s = []
ss = []

def f():
    if len(s) == m and set(s) not in ss:
        print(" ".join(map(str,s)))
        ss.append(set(s))
        return
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            f()
            s.pop()

f()
