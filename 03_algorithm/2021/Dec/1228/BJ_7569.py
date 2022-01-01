from collections import deque

M, N, H = map(int, input().split())
dr = [-1, 1, 0, 0, -N, N]
dc = [0, 0, -1, 1, 0, 0]


def bfs():
    global grown_tomato_cnt
    global visited
    while qu:
        r, c, days = qu.popleft()
        tmp = r // N
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= (tmp+1) * N or nr < tmp * N or nc >= M or nc < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == -1: continue
            visited[nr][nc] = 1
            grown_tomato_cnt += 1
            qu.append([nr, nc, days + 1])
        for i in range(4,6):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N * H or nr < 0 or visited[nr][nc] == 1 or MAP[nr][nc] == -1: continue
            visited[nr][nc] = 1
            grown_tomato_cnt += 1
            qu.append([nr, nc, days + 1])
    return days


MAP = [list(map(int, input().split())) for _ in range(N * H)]
all_tomato_cnt = 0
grown_tomato_cnt = 0
qu = deque()
visited = [[0] * M for _ in range(N * H)]
for n in range(N * H):
    for m in range(M):
        if MAP[n][m] == 1:
            grown_tomato_cnt += 1
            all_tomato_cnt += 1
            visited[n][m] = 1
            qu.append([n, m, 0])
        elif MAP[n][m] == 0:
            all_tomato_cnt += 1
if all_tomato_cnt == grown_tomato_cnt:
    print(0)
else:
    if grown_tomato_cnt == 0:
        print(-1)
    else:
        ret = bfs()
        if all_tomato_cnt == grown_tomato_cnt:
            print(ret)
        else:
            print(-1)
