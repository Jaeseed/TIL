from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(step, s_idx, now_list):
    global MAP
    if step == M:
        bfs(now_list)
        return
    for v in range(s_idx, virus_cnt):
        nr, nc = virus_tong[v]
        MAP[nr][nc] = -1
        dfs(step + 1, v + 1, now_list + [[nr, nc]])
        MAP[nr][nc] = 2
    return


def bfs(now_list):
    global flag
    global min_seconds
    if empty_cnt == 0:
        flag = 1
        min_seconds = 0
        return
    now_empty_cnt = empty_cnt
    qu = deque()
    visited = [[0] * N for _ in range(N)]
    for r, c in now_list:
        qu.append([r, c, 0])
        visited[r][c] = 1
    while qu:
        r_, c_, cnt = qu.popleft()
        for i in range(4):
            nr = r_ + dr[i]
            nc = c_ + dc[i]
            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == 1: continue
            if MAP[nr][nc] == 0:
                now_empty_cnt -= 1
                if now_empty_cnt == 0:
                    min_seconds = min(min_seconds, cnt+1)
                    flag = 1
                    break
            visited[nr][nc] = 1
            qu.append([nr, nc, cnt + 1])
    return


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
virus_tong = []
flag = 0
empty_cnt = 0
for row in range(N):
    for col in range(N):
        if MAP[row][col] == 2:
            virus_tong.append([row, col])
        elif MAP[row][col] == 0:
            empty_cnt += 1
min_seconds = 2e29
virus_cnt = len(virus_tong)
dfs(0, 0, list())
if flag == 1:
    print(min_seconds)
else:
    print(-1)
