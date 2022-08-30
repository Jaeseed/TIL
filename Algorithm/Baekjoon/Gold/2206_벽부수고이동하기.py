from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    qu = deque()
    qu.append([0, 0, 1, 0])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while qu:
        r, c, cnt, is_broken = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0: continue
            if visited[nr][nc]:
                if visited[nr][nc] != 2 or is_broken == 1:
                    continue
            if MAP[nr][nc] == 1:
                if is_broken:
                    continue
                else:
                    visited[nr][nc] = 2
                    qu.append([nr, nc, cnt + 1, 1])
            else:
                visited[nr][nc] = 1
                qu.append([nr, nc, cnt + 1, is_broken])
            if nr == N -1 and nc == M - 1:
                return cnt + 1
    return -1


N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
answer = 0
print(bfs())
