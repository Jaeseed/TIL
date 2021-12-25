from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    visited = [[0] * M for _ in range(N)]
    qu = deque()
    qu.append([0, 0, 1])
    visited[0][0] = 1
    while qu:
        r, c, cnt = qu.popleft()
        if r == N - 1 and c == M - 1:
            return cnt
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or MAP[nr][nc] == '0' or visited[nr][nc] == 1: continue
            qu.append([nr, nc, cnt + 1])
            visited[nr][nc] = 1


N, M = map(int, input().split())
MAP = [input() for _ in range(N)]
ret = bfs()
print(ret)
