from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    qu = deque()
    goal = [N - 1, M - 1]
    qu.append([0, 0, 1])
    while True:
        r, c, cnt = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or MAP[nr][nc] == '0' or visited[nr][nc] == 1: continue
            if nr == goal[0] and nc == goal[1]:
                return cnt + 1
            visited[nr][nc] = 1
            qu.append([nr, nc, cnt + 1])


N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
answer = bfs()
print(answer)
