from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    qu = deque()
    qu.append(coin_spot + [0])
    while True:
        r1, c1, r2, c2, step = qu.popleft()
        if step == 10:
            return -1
        for i in range(4):
            nr1 = r1 + dr[i]
            nc1 = c1 + dc[i]
            nr2 = r2 + dr[i]
            nc2 = c2 + dc[i]
            nr1, nc1 = check(r1, c1, nr1, nc1)
            nr2, nc2 = check(r2, c2, nr2, nc2)
            if nr1 + nr2 == -2:
                continue
            elif nr1 == -1 or nr2 == -1:
                return step + 1
            qu.append([nr1, nc1, nr2, nc2, step + 1])


def check(r, c, nr, nc):
    if nr >= N or nr < 0 or nc >= M or nc < 0:
        return -1, -1
    elif MAP[nr][nc] == '#':
        return r, c
    else:
        return nr, nc


N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
coin_spot = []
for n in range(N):
    for m in range(M):
        if MAP[n][m] == 'o':
            coin_spot += [n, m]
            MAP[n][m] = '.'
    if len(coin_spot) == 4:
        break
ret = bfs()
print(ret)