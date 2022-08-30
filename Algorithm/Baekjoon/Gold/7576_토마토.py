from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global cnt, MAP
    qu = deque()
    for tomato in tomato_tong:
        qu.append(tomato + [0])
    day = 0
    while qu:
        r, c, day = qu.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0 or MAP[nr][nc] == -1 or MAP[nr][nc] == 1:
                continue
            MAP[nr][nc] = 1
            cnt += 1
            if cnt == max_cnt:
                return day + 1
            qu.append([nr, nc, day + 1])
    return day


M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
tomato_tong = []
cnt = 0
max_cnt = 0
for n in range(N):
    for m in range(M):
        if MAP[n][m] == 0 or MAP[n][m] == 1:
            max_cnt += 1
            if MAP[n][m] == 1:
                tomato_tong.append([n, m])
                cnt += 1
answer = bfs()
if cnt != max_cnt:
    print(-1)
else:
    print(answer)