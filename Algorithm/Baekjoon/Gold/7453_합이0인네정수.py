import sys


def dfs(step, num):
    if step == 3:
        search()
        return
    return


def search():
    return


N = int(input())
A, B, C, D = [], [], [], []
for n in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
A.sort()
B.sort()
C.sort()
D.sort()
dfs(0, '')
