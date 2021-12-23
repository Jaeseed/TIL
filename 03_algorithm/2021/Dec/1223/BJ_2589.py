from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    qu = deque()
    qu.append([row, col, 0])
    used = [[0] * M for _ in range(N)]
    used[row][col] = 1
    while qu:
        r, c, time = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or used[nr][nc] == 1 or MAP[nr][nc] == 'W': continue
            qu.append([nr, nc, time + 1])
            used[nr][nc] = 1
    return time


N, M = map(int, input().split())
MAP = [input() for _ in range(N)]
max_time = 0
for n in range(N):
    for m in range(M):
        if MAP[n][m] == 'L':
            if m != 0 and m != M-1:
                if MAP[n][m-1] == 'L' and MAP[n][m+1] == 'L':
                    continue
            if n != 0 and n != N-1:
                if MAP[n-1][m] == 'L' and MAP[n+1][m] == 'L':
                    continue
            ret = bfs(n, m)
            if max_time < ret:
                max_time = ret
print(max_time)
