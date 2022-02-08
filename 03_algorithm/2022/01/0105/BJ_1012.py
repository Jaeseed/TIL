import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global visited
    visited[r][c] = 1
    qu = deque()
    qu.append([r, c])
    while qu:
        r, c = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 0: continue
            qu.append([nr, nc])
            visited[nr][nc] = 1


T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    MAP = [[0] * M for _ in range(N)]
    ans = 0
    visited = [[0] * M for _ in range(N)]
    for k in range(K):
        col, row = map(int, sys.stdin.readline().split())
        MAP[row][col] = 1
    for row in range(N):
        for col in range(M):
            if MAP[row][col] == 1 and visited[row][col] == 0:
                bfs(row, col)
                ans += 1
    print(ans)