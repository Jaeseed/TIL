from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(ro, co, target):
    global visited
    qu = deque()
    qu.append([ro, co])
    while qu:
        row, col = qu.popleft()
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] or MAP[nr][nc] not in target: continue
            qu.append([nr, nc])
            visited[nr][nc] = 1
    return


N = int(input())
MAP = [list(input()) for _ in range(N)]
answer = [0, 0]
# 1. 정상인
visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            bfs(r, c, [MAP[r][c]])
            answer[0] += 1
# 2. 적록색약
visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            if MAP[r][c] == 'R' or MAP[r][c] == 'G':
                bfs(r, c, ['R', 'G'])
            else:
                bfs(r, c, ['B'])
            answer[1] += 1
print(' '.join(map(str, answer)))
